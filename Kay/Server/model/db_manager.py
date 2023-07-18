import sqlite3
from pathlib import Path


def store_in_database(email, hashed_password, salt):
    # Connect to the SQLite database
    # If the database does not exist, it will be created
    conn = sqlite3.connect(f'{str(Path(__file__).parents[1])}/database/user_database.db')

    # Create a cursor object
    c = conn.cursor()

    # Create a table named 'users' if it does not exist
    # The table has columns for email, hashed_password, and salt
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            hashed_password TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    ''')

    # Insert the user's data into the 'users' table
    c.execute('''
        INSERT INTO users (email, hashed_password, salt)
        VALUES (?, ?, ?)
    ''', (email, hashed_password, salt))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    

def check_user(email):
    # Connect to the SQLite database
    conn = sqlite3.connect(f'{str(Path(__file__).parents[1])}/database/user_database.db')

    # Create a cursor object
    c = conn.cursor()

    # Execute a SELECT statement to check if a user with the given email exists
    c.execute('''
        SELECT * FROM users WHERE email = ?
    ''', (email,))

    # Fetch one record, if any
    record = c.fetchone()

    # Close the connection to the database
    conn.close()
    
    return record


def get_userInfo(email):
    # Connect to the SQLite database
    conn = sqlite3.connect(f'{str(Path(__file__).parents[1])}/database/user_database.db')

    # Create a cursor object
    c = conn.cursor()

    # Execute a SELECT statement to get the user's data
    c.execute('''
        SELECT email, hashed_password, salt FROM users WHERE email = ?
    ''', (email,))

    # Fetch one record
    record = c.fetchone()

    # Close the connection to the database
    conn.close()
    
    return record