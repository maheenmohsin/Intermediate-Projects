import os

# File name for storing contacts
CONTACT_FILE = "contacts.txt"

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    with open(CONTACT_FILE, "a") as f:
        f.write(f"{name},{phone},{email}\n")
    print("✅ Contact added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not os.path.exists(CONTACT_FILE):
        print("❌ No contacts found.\n")
        return
    with open(CONTACT_FILE, "r") as f:
        contacts = f.readlines()
        if not contacts:
            print("❌ No contacts found.\n")
        else:
            print("\n📖 Saved Contacts:")
            for idx, contact in enumerate(contacts, start=1):
                name, phone, email = contact.strip().split(",")
                print(f"{idx}. {name} | {phone} | {email}")
            print()

# Function to search for a contact
def search_contact():
    search = input("Enter name or phone to search: ").lower()
    found = False
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            for contact in f:
                name, phone, email = contact.strip().split(",")
                if search in name.lower() or search in phone:
                    print(f"✅ Found: {name} | {phone} | {email}")
                    found = True
    if not found:
        print("❌ Contact not found.\n")

# Function to delete a contact
def delete_contact():
    search = input("Enter name of contact to delete: ").lower()
    updated_contacts = []
    found = False
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            contacts = f.readlines()
        with open(CONTACT_FILE, "w") as f:
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                if search != name.lower():
                    f.write(contact)
                else:
                    found = True
        if found:
            print("✅ Contact deleted successfully!\n")
        else:
            print("❌ Contact not found.\n")
    else:
        print("❌ No contacts available.\n")

# Main program loop
def main():
    while True:
        print("📒 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
