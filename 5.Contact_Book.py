contacts = []

def add_contact():
    print("Add a new contact:")
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    print("List of contacts:")
    if not contacts:
        print("No contacts found.\n")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()

def search_contact():
    search_term = input("Enter the name to search: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['name'].lower():
            found_contacts.append(contact)
    
    if not found_contacts:
        print(f"No contacts found with the name '{search_term}'.\n")
    else:
        print(f"Found {len(found_contacts)} contact(s) with the name '{search_term}':")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()

def update_contact():
    search_term = input("Enter the name of the contact to update: ")
    found_index = -1
    for index, contact in enumerate(contacts):
        if search_term.lower() == contact['name'].lower():
            found_index = index
            break
    
    if found_index == -1:
        print(f"No contact found with the name '{search_term}'.\n")
    else:
        print(f"Current details of '{contacts[found_index]['name']}':")
        print(f"Name: {contacts[found_index]['name']}, Phone: {contacts[found_index]['phone']}, Email: {contacts[found_index]['email']}")
        print("Enter new details (leave blank to keep current):")
        name = input(f"Name ({contacts[found_index]['name']}): ") or contacts[found_index]['name']
        phone = input(f"Phone ({contacts[found_index]['phone']}): ") or contacts[found_index]['phone']
        email = input(f"Email ({contacts[found_index]['email']}): ") or contacts[found_index]['email']
        
        contacts[found_index]['name'] = name
        contacts[found_index]['phone'] = phone
        contacts[found_index]['email'] = email
        print(f"Contact '{name}' updated successfully!\n")

def delete_contact():
    search_term = input("Enter the name of the contact to delete: ")
    found_index = -1
    for index, contact in enumerate(contacts):
        if search_term.lower() == contact['name'].lower():
            found_index = index
            break
    
    if found_index == -1:
        print(f"No contact found with the name '{search_term}'.\n")
    else:
        del contacts[found_index]
        print(f"Contact '{search_term}' deleted successfully!\n")

# Main menu loop
while True:
    print("Welcome to the Contact Book")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Thank you for using the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")