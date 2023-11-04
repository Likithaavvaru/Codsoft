# Initialize an empty contact book
contact_book = {}

# Function to add a new contact
def add_contact(contact_book, name, phone_number):
    contact_book[name] = phone_number
    print(f"Added {name} to the contact book.")

# Function to display all contacts
def display_contacts(contact_book):
    if not contact_book:
        print("Contact book is empty.")
    else:
        print("Contacts:")
        for name, phone_number in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone Number: {phone_number}")
            print()

# Function to search for a contact
def search_contact(contact_book, name):
    if name in contact_book:
        print("Contact found:")
        print(f"Name: {name}")
        print(f"Phone Number: {contact_book[name]}")
    else:
        print(f"Contact with name '{name}' not found in the contact book.")

# Function to delete a contact
def delete_contact(contact_book, name):
    if name in contact_book:
        del contact_book[name]
        print(f"{name} has been deleted from the contact book.")
    else:
        print(f"Contact with name '{name}' not found in the contact book.")

# Main menu
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        add_contact(contact_book, name, phone_number)
    elif choice == '2':
        display_contacts(contact_book)
    elif choice == '3':
        name = input("Enter the name to search for: ")
        search_contact(contact_book, name)
    elif choice == '4':
        name = input("Enter the name to delete: ")
        delete_contact(contact_book, name)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4/5).")
