import hashlib


def hash_password(password: str, salt: str) -> str:
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    return hashlib.pbkdf2_hmac('sha256', password_bytes, salt_bytes, 100000).hex()