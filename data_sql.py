import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
try:
    db = mysql.connector.connect(
        host=os.getenv("DB_Host", "localhost"),
        user=os.getenv("DB_User", "root"),
        password=os.getenv("DB_Password", "admin"),
        port=os.getenv("DB_Port", "3306")
    )
    cursor = db.cursor(dictionary=True)

    print("Connected to MySQL database successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)  # Exit the script if connection fails

def create_db():
    database = os.getenv("DB_Name", "contacts_app")
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    cursor.execute(f"USE {database}")
    db.commit()

def create_contacts_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        number INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20),
        email VARCHAR(255),
        gender VARCHAR(10),
        photo VARCHAR(255)
    );
    """)
    db.commit()

# Ensure both the database and the table are created
create_db()
create_contacts_table()

def get_contacts():
    cursor.execute("SELECT * FROM contacts")
    return cursor.fetchall()

def find_by_number(number):
    cursor.execute("SELECT * FROM contacts WHERE number = %s", (number,))
    return cursor.fetchone()

def search_contacts(search_name):
    cursor.execute("SELECT * FROM contacts WHERE name LIKE %s", (f"%{search_name}%",))
    return cursor.fetchall()

def create_contact(name, phone, email, gender, photo):
    cursor.execute(
        "INSERT INTO contacts (name, phone, email, gender, photo) VALUES (%s, %s, %s, %s, %s)",
        (name, phone, email, gender, photo)
    )
    db.commit()


def delete_contact(number):
    cursor.execute("DELETE FROM contacts WHERE number = %s", (number,))
    db.commit()

def contact_exists(name, email):
    cursor.execute("SELECT * FROM contacts WHERE name = %s OR email = %s", (name, email))
    return cursor.fetchone() is not None

def update_contact(number, name, phone, email, gender):
    cursor.execute("UPDATE contacts SET name = %s, phone = %s, email = %s, gender = %s WHERE number = %s",
                   (name, phone, email, gender, number))
    db.commit()
