# Define Content Security Policy (CSP)
CSP_POLICICY = {
    'default-src': ["'self'"],
    'style-src': ["'self'","https://stackpath.bootstrapcdn.com","'unsafe-inline'"],
    'script-src': ["'self'","https://code.jquery.com","https://stackpath.bootstrapcdn.com"],
    'img-src': ["'self'", 'data:'],
    'font-src': ["'self'", 'data:'],
    'object-src': ["'none'"],
    'frame-src': ["'none'"],
    'base-uri': ["'self'"],
    'form-action': ["'self'"],
    'frame-ancestors': ["'none'"],
    'manifest-src': ["'self'"],
}

DATABASE_KEYWORD = 'impenetrable_07062024'

file_path = 'xss_payload_patterns.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

XSS_PATTERNS = [line.strip() for line in lines]

BLOCKED_PATTERN = [
        DATABASE_KEYWORD,
        r'substr(ing)?\(.*\)',
        r'(current|session|pg)_user',
        r'information_schema',
        r'pg_(user|shadow|database|class|namespace|attribute|type|catalog|toast)',
        r'current_database\(.*\)',
        r'getpgusername\(.*\)',
        r'pg_sleep\(.*\)',
        r'(query|database)_to_xml\(.*\)',
        r'cast\(.*\)',
        r'select.*from',
        r'version\(.*\)',
        r'copy.*from',
        r'current_setting\(.*\)',
        r'inet_server_(port|addr)\(.*\)',
        r'(create|drop|truncate).*(table|database)',
        r'<script.*</script>'
]

BLOCKED_PATTERN.extend(XSS_PATTERNS)