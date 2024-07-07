from hypercorn.asyncio import serve
from hypercorn.config import Config
from app import app  # Import your Quart application instance

config_dict = {
    'bind': '0.0.0.0:80',    # Bind to localhost on port 80
    'workers': 2,              # Number of worker processes
    'loglevel': 'info',        # Log level (debug, info, warning, error, critical)
    'accesslog': '-',          # Log access to stdout
    'errorlog': '-',           # Log errors to stdout
    'use_reloader': True,      # Enable auto-reloading
    'use_colors': True,        # Use colored output in the console
    'include_server_header': False  # Exclude server header
}

async def run():
    config = Config.from_mapping(config_dict)
    await serve(app, config)

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
