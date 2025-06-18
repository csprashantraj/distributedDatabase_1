import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from config import get_aes_key
from decimal import Decimal  # Add this import

def decrypt_data(encrypted_blob):
    """Decrypt Base64-encoded AES-GCM data with precise number handling."""
    key = get_aes_key()
    decoded_data = base64.b64decode(encrypted_blob)

    iv = decoded_data[:12]
    tag = decoded_data[-16:]
    ciphertext = decoded_data[12:-16]

    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Convert back to Decimal for precise number handling
    try:
        return str(Decimal(decrypted_data.decode()))
    except:
        return decrypted_data.decode()

if __name__ == '__main__':
    encrypted_data = "Paste_Encrypted_String_Here"

    try:
        decrypted_data = decrypt_data(encrypted_data)
        print(f" Decrypted Data: {decrypted_data}")
    except Exception as e:
        print(f" Decryption Failed: {e}")
