import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from config import get_aes_key
from decimal import Decimal  # Add this import

def encrypt_data(data):
    """Encrypt data using AES-GCM with precise number handling."""
    # Convert number to exact string representation
    if isinstance(data, (int, Decimal)):
        data = format(Decimal(str(data)), 'f')
    
    key = get_aes_key()
    iv = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Ensure we're using exact string representation
    ciphertext = encryptor.update(str(data).encode()) + encryptor.finalize()
    tag = encryptor.tag

    encrypted_blob = base64.b64encode(iv + ciphertext + tag).decode()
    return encrypted_blob

if __name__ == '__main__':
    data = "Sensitive Data"
    
    encrypted_data = encrypt_data(data)
    print(f" Encrypted Data: {encrypted_data}")
