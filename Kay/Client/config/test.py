import os
import hashlib

def hash_password(salt: str) -> str:
        password_bytes = 'Aa123456!'.encode('utf-8')
        salt_bytes = salt.encode('utf-8')
        return hashlib.pbkdf2_hmac('sha256', password_bytes, salt_bytes, 100000, dklen=64).hex()

def encrypt_password():
    # Generate a salt
    salt = os.urandom(16).hex()

    # Hash the password with the salt
    hashed_password = hash_password(salt)
    return hashed_password, salt

a = encrypt_password()
print(a)