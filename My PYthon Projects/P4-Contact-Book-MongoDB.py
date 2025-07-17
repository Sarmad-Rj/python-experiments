from pymongo import MongoClient

# MongoDB connection
client = MongoClient(connection)
db = client["contact_book_db"]
contacts_col = db["contacts"]


# Add new contact
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    result = contacts_col.insert_one(contact)
    print(f"\n Contact added successfully with ID: {result.inserted_id}\n")

# Show all contacts
def show_contacts():
    contacts = list(contacts_col.find())
    if contacts:
        print("\n Contact List:")
        for idx, contact in enumerate(contacts, 1):
            print(f"""
[{idx}]
Name: {contact.get('name')}
Phone: {contact.get('phone')}
Email: {contact.get('email')}
Address: {contact.get('address')}
---------------------------""")
    else:
        print("\n No contacts found.\n")

# Update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    contact = contacts_col.find_one({"name": name})

    if contact:
        print("\nLeave fields empty to keep current values.\n")
        new_phone = input(f"New phone [{contact.get('phone')}]: ").strip() or contact.get('phone')
        new_email = input(f"New email [{contact.get('email')}]: ").strip() or contact.get('email')
        new_address = input(f"New address [{contact.get('address')}]: ").strip() or contact.get('address')

        contacts_col.update_one(
            {"_id": contact["_id"]},
            {"$set": {
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            }}
        )
        print("\n Contact updated successfully.\n")
    else:
        print("\n Contact not found.\n")

# Delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    contact = contacts_col.find_one({"name": name})

    if contact:
        confirm = input(f"Are you sure you want to delete {name}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            contacts_col.delete_one({"_id": contact["_id"]})
            print("\n Contact deleted successfully.\n")
        else:
            print("\nDeletion cancelled.\n")
    else:
        print("\n Contact not found.\n")

# Main CLI loop
def main():
    while True:
        print("""
===== Contact Book Menu =====
1. Add a new contact
2. Show all contacts
3. Update a contact
4. Delete a contact
5. Exit
""")
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("\n Exiting Contact Book. Goodbye!\n")
            break
        else:
            print("\n Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()