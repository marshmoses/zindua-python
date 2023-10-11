phonebook = {}  # Initialize an empty phonebook dictionary

def add_contact():
    name = input("Enter the contact name: ")
    number = input("Enter the phone number: ")
    
    if name in phonebook:
        print(f"{name} is already in the phonebook.")
    else:
        phonebook[name] = number
        print(f"{name} has been added to the phonebook.")

def delete_contact():
    name = input("Enter the contact name to delete: ")
    
    if name in phonebook:
        del phonebook[name]
        print(f"{name} has been deleted from the phonebook.")
    else:
        print(f"{name} is not found in the phonebook.")

def search_contact():
    name = input("Enter the contact name to search: ")
    
    if name in phonebook:
        print(f"Phone number for {name}: {phonebook[name]}")
    else:
        print(f"{name} is not found in the phonebook.")

def print_contacts():
    print("Phonebook Contacts:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

while True:
    print("\nPhonebook App Menu:")
    print("1. Add a Contact")
    print("2. Delete a Contact")
    print("3. Search for a Contact")
    print("4. Print All Contacts")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        delete_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print_contacts()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4/5).")
