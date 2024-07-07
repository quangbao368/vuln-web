class HTTPSecurityHeaderMiddleware:
    def __init__(self, app, csp_policy):
        self.app = app
        self.csp_policy = csp_policy

    async def __call__(self, scope, receive, send):
        async def custom_send(message):
            if message['type'] == 'http.response.start':
                headers = [(name, value) for name, value in message.get('headers', []) if name != b"server"]
                
                # Adding CSP headers
                headers.append((b'content-security-policy', self._build_csp_header().encode()))
                
                # Set server header
                headers.append((b'server', b'vuln-web'))
                
                message['headers'] = headers
            
            await send(message)
        
        if scope['type'] in ['http', 'websocket']:
            await self.app(scope, receive, custom_send)
        else:
            await self.app(scope, receive, send)
    
    def _build_csp_header(self):
        csp_directives = []
        for directive, sources in self.csp_policy.items():
            csp_directives.append(f"{directive} {' '.join(sources)}")
        return "; ".join(csp_directives)
