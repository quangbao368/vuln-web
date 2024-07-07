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

TAG_EVENTS = {'onpointerrawupdate', 'ontoggle', 'onclick', 'onpointerover', 'onfocusout', 'onloadedmetadata', 'onpageshow', 'onsubmit', 'oncontextmenu', 'onpointerup', 'onreset', 'onanimationend', 'onload', 'oninput', 'ontransitionend', 'onselectstart', 'onmousewheel', 'onpointerdown', 'onformdata', 'ontransitionstart', 'ondrag', 'onerror', 'ondragstart', 'onkeyup', 'onwebkittransitionend', 'ontouchend', 'oncanplaythrough', 'onbeforeinput', 'onanimationiteration', 'onbeforescriptexecute', 'onunhandledrejection', 'onbeforetoggle', 'onprogress', 'onbegin', 'oncanplay', 'onshow', 'ondragend', 'onblur', 'onpaste', 'onwebkitanimationend', 'src/onerror', 'onwebkitplaybacktargetavailabilitychanged', 'onplay', 'ontouchmove', 'onratechange', 'onkeypress', 'onmousedown', 'onwebkitmouseforcewillbegin', 'onafterscriptexecute', 'onloadstart', 'onfocusin', 'onvolumechange', 'onselect', 'onfocus', 'onpointerleave', 'onclose', 'oninvalid', 'onscroll', 'onwebkitanimationiteration', 'onafterprint', 'onselectionchange', 'onplaying', 'ontouchstart', 'oncut', 'onbeforecut', 'onended', 'onmousemove', 'onwebkitwillrevealbottom', 'oncuechange', 'onseeked', 'onmouseleave', 'onsearch', 'onanimationstart', 'onloadeddata', 'onwheel', 'ontimeupdate', 'ondragexit', 'ondblclick', 'ondragleave', 'onmouseenter', 'onmouseout', 'onsuspend', 'onseeking', 'onfullscreenchange', 'onwebkitanimationstart', 'onmouseover', 'onwebkitmouseforcedown', 'onpointerout', 'ondurationchange', 'onmozfullscreenchange', 'onpause', 'onscrollend', 'ondrop', 'onpointercancel', 'onkeydown', 'ondragenter', 'onbeforecopy', 'onpointermove', 'onmouseup', 'onchange', 'onauxclick', 'onend', 'oncopy', 'onwebkitmouseforceup', 'onwebkitmouseforcechanged', 'ondragover', 'onrepeat', 'onpointerenter'}


file_path = 'xss_payload_patterns.txt'
with open(file_path, 'r') as file:
    # Read all lines from the file into a list
    lines = file.readlines()

# Strip newline characters from each line
XSS_PATTERNS = [line.strip() for line in lines]

BLOCKED_PATTERN = [
        DATABASE_KEYWORD,
        'substr',
        'current_user',
        'session_user',
        'pg_user',
        'information_schema',
        'pg_database',
        'current_database',
        'pg_sleep',
        'SUBSTRING',
        r'cast([a-z0-9\s\t().]+)',
        r'select.*from',
        r'version(.*)',
        'copy.*from',
        r'create.*(table|database)',
        r'<script.*</script>',
    ]

BLOCKED_PATTERN.extend(XSS_PATTERNS)