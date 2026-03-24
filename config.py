# config.py (UPDATED)

import os
from dotenv import load_dotenv

load_dotenv(".env")

class Config:
    API_ID = int(os.environ.get("8601508249", 0))
    API_HASH = os.environ.get("AAG2pzKH0PRzgiQ9bYJvgevSUEScTGUZ86g")
    BOT_TOKEN = os.environ.get("8601508249:AAG2pzKH0PRzgiQ9bYJvgevSUEScTGUZ86g", "")
    OWNER_ID = int(os.environ.get("7888588771", 0))
    
    _storage_channel_str = os.environ.get("shelbyyyyyyy1")
    if _storage_channel_str:
        try: STORAGE_CHANNEL = int(shelbyyyyyyy1)
        except ValueError: STORAGE_CHANNEL = _storage_channel_str
    else: STORAGE_CHANNEL = 1
    
    BASE_URL = os.environ.get("BASE_URL", "").rstrip('/')
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    REDIRECT_BLOGGER_URL = os.environ.get("REDIRECT_BLOGGER_URL", "")
    BLOGGER_PAGE_URL = os.environ.get("BLOGGER_PAGE_URL", "")
    
    # --- YAHAN BADLAV KIYA GAYA HAI ---
    # Force Subscribe ke liye channel ID/username
    _fsub_channel_str = os.environ.get("FORCE_SUB_CHANNEL")
    if _fsub_channel_str:
        try: FORCE_SUB_CHANNEL = int(_fsub_channel_str)
        except ValueError: FORCE_SUB_CHANNEL = _fsub_channel_str
    else: FORCE_SUB_CHANNEL = 0
        
    # Yeh bot ka username store karega (code isse automatic set karega)
    BOT_USERNAME = ""
