import os
import base64
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

def get_aes_key():
    """Retrieve AES key from .env and decode it from Base64."""
    key_b64 = os.getenv("AES_KEY")
    if not key_b64:
        raise ValueError("AES_KEY is missing from .env!")
    
    key_bytes = base64.b64decode(key_b64)
    if len(key_bytes) != 32:
        raise ValueError("AES_KEY must be exactly 32 bytes (AES-256)!")
    
    return key_bytes