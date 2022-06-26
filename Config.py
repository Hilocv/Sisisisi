import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
else:
    # Fill the Values
    API_ID = 14681595
    API_HASH = "a86730aab5c59953c424abb4396d32d5"
    BOT_TOKEN = "5362722840:AAGM04PCx8pQNdGKGPqGFBvLxjW36AO8dpo"
