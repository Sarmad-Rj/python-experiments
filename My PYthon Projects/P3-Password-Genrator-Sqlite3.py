import sqlite3
import random

CHARS = "qwertyuiopasdfghjklzxcvbnm[]QWERTYUIOPASDFGHJKLZXCVBNM}{;',./<>?:1234567890!@#$%^&*()_+-="

DB_NAME = "passwords.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def generate_password(length):
    return ''.join(random.choice(CHARS) for _ in range(length))

def save_password(platform, username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO passwords (platform, username, password) VALUES (?, ?, ?)',
              (platform, username, password))
    conn.commit()
    conn.close()
    print("Password saved successfully.\n")

def show_passwords():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM passwords')
    rows = c.fetchall()
    if rows:
        print("~"*70)
        for row in rows:
            print(f"ID: {row[0]} | Platform: {row[1]} | Username: {row[2]} | Password: {row[3]}")
        print("~"*70)
    else:
        print("No passwords saved yet.")
    conn.close()

def update_password():
    show_passwords()
    id_ = input("Enter the ID of the password you want to update: ")
    platform = input("New platform: ")
    username = input("New username: ")
    password = input("New password: ")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('UPDATE passwords SET platform = ?, username = ?, password = ? WHERE id = ?',
              (platform, username, password, id_))
    conn.commit()
    conn.close()
    print("Password updated successfully.\n")

def delete_password():
    show_passwords()
    id_ = input("Enter the ID of the password you want to delete: ")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM passwords WHERE id = ?', (id_,))
    conn.commit()
    conn.close()
    print("Password deleted successfully.\n")

def main():
    create_table()
    while True:
        print("~" * 50) 
        print("===== Password Manager =====")
        print("1. Generate a password")
        print("2. Generate and save a password")
        print("3. Show saved passwords")
        print("4. Update a password entry")
        print("5. Delete a password entry")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("~" * 50)
            length = int(input("Enter password length: "))
            pwd = generate_password(length)
            print(f'Generated password: "{pwd}"')
            save = input("Do you want to save this password? (yes/no): ").lower()
            if save == 'yes':
                platform = input("Enter platform name: ")
                username = input("Enter username: ")
                save_password(platform, username, pwd)

        elif choice == '2':
            print("~" * 50)
            length = int(input("Enter password length: "))
            pwd = generate_password(length)
            print(f"Generated password: {pwd}")
            platform = input("Enter platform name: ")
            username = input("Enter username: ")
            save_password(platform, username, pwd)

        elif choice == '3':
            print("~" * 50)
            show_passwords()

        elif choice == '4':
            print("~" * 50)
            update_password()

        elif choice == '5':
            print("~" * 50)
            delete_password()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
