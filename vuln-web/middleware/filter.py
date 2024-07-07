import re
from urllib.parse import unquote_plus
from defination import BLOCKED_PATTERN


class FilterMiddleware:


    def __init__(self, app):
        self.app = app
    
    
    
    def contains_blocked_pattern(self, body:bytes, content_type):
        # Decode body based on content type
        
        if content_type == b'application/x-www-form-urlencoded':
            body = unquote_plus(body.decode('utf-8', errors='replace'))
        else:
            body :str = body.decode('unicode-escape',errors="replace")

        for pattern in BLOCKED_PATTERN:
            if re.search(pattern, body, re.IGNORECASE | re.MULTILINE):
                return True
        return False
    
    async def __call__(self, scope, receive, send):
        if scope['type'] == 'http':
            
            
            query_params = scope.get('query_string', b'')
            
            if query_params:
                for param in query_params.split(b'&'):
                    tokens = param.split(b'=')
                    if len(tokens) != 2:
                        continue
                    value = tokens[1]
                    if self.contains_blocked_pattern(value,b'application/x-www-form-urlencoded'):
                        return await self.error_response(send)
                    # Check path parameters (assuming path is decoded UTF-8)
            
            path = scope['path']
            if path and self.contains_blocked_pattern(path.encode(), b'application/x-www-form-urlencoded'):
                return await self.error_response(send)
            
            
            
            body : bytes= await self.get_request_body(receive)
            content_type = dict(scope['headers']).get(b'content-type', b'application/x-www-form-urlencoded')

            if len(body) <= 2500 and self.contains_blocked_pattern(body, content_type):
                return await self.error_response(send)
            
            # Reconstruct the receive function with the read body for the downstream app
            receive = self.create_receive(body, receive)
            
        
        return await self.app(scope, receive, send)

    

    async def get_request_body(self, receive):
        body = b''
        more_body = True
        while more_body:
            message = await receive()
            if message['type'] == 'http.request':
                body += message.get('body', b'')
                more_body = message.get('more_body', False)
        return body

    def create_receive(self, body, receive):
        async def new_receive():
            nonlocal body
            if body:
                chunk = body[:65536]
                body = body[65536:]
                return {
                    'type': 'http.request',
                    'body': chunk,
                    'more_body': bool(body)
                }
            return await receive()
        return new_receive



    async def error_response(self, send):
        msg = b'blocked'
        content_length = len(msg)
        await send({
            'type': 'http.response.start',
            'status': 401,
            'headers': [(b'content-length', str(content_length).encode())],
        })
        await send({
            'type': 'http.response.body',
            'body': msg,
            'more_body': False,
        })