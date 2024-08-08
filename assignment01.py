def add_contact(contact_dict, name, phone, email):
    contact_dict[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully!")

def update_contact(contact_dict, name, phone=None, email=None):
    if name in contact_dict:
        if phone:
            contact_dict[name]['phone'] = phone
        if email:
            contact_dict[name]['email'] = email
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found!")

def delete_contact(contact_dict, name):
    if name in contact_dict:
        del contact_dict[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found!")

def search_contact(contact_dict, name):
    if name in contact_dict:
        print(f"Name: {name}, Phone: {contact_dict[name]['phone']}, Email: {contact_dict[name]['email']}")
    else:
        print(f"Contact '{name}' not found!")

def display_contacts(contact_dict):
    if contact_dict:
        print("\nAll contacts:")
        for name, details in contact_dict.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts found.")


def main():
    contacts = {}

    while True:
        print("\n1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            add_contact(contacts, name, phone, email)
        elif choice == '2':
            name = input("Enter name of the contact to update: ").strip()
            phone = input("Enter new phone number (leave blank to skip): ").strip()
            email = input("Enter new email (leave blank to skip): ").strip()
            update_contact(contacts, name, phone or None, email or None)
        elif choice == '3':
            name = input("Enter name of the contact to delete: ").strip()
            delete_contact(contacts, name)
        elif choice == '4':
            name = input("Enter name to search: ").strip()
            search_contact(contacts, name)
        elif choice == '5':
            display_contacts(contacts)
        elif choice == '6':
            print("Exiting the contact management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
