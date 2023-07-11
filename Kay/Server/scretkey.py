import os
import sqlite3
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("secret.key"):
        generate_key()
    return open("secret.key", "rb").read()

def encrypt_password(password: str) -> bytes:
    cipher_text = cipher_suite.encrypt(password.encode())
    return cipher_text

def decrypt_password(cipher_text: bytes) -> str:
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text.decode()

def create_user(username: str, password: str):
    encrypted_password = encrypt_password(password)
    
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password BLOB)")
    cursor.execute("INSERT INTO users VALUES (?,?)", (username, encrypted_password))
    
    conn.commit()
    conn.close()

def get_password(username: str) -> str:
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result is None:
        print("User not found")
        return None
    
    encrypted_password = result[0]
    password = decrypt_password(encrypted_password)
    
    return password

key = load_key()
cipher_suite = Fernet(key)
create_user("9350816", "Wjddydrnr9(")
pwd = get_password("9350816")
print(pwd)