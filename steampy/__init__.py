


SteamApiKey = ""



def set_api_key(api_key):
    global SteamApiKey
    if not isinstance(api_key, str):
        raise ValueError("API key must be a string.")
    if api_key is None or "":
        raise ValueError("API key cannot be empty.")
    else:
        SteamApiKey = api_key



def get_api_key():
    global SteamApiKey
    if SteamApiKey is None or "":
        raise ValueError("API key not set. Please set it before using.")
    return SteamApiKey

