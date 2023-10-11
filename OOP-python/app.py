#                                     import csv
#import csv
#class phonebook:
#    def __init__(self,name,number,):
#      self.name=name
 #     self.number=number



#class phonebookapp:
   # def __init__(self):
     #   self.phonebook=[]

    #def add_item(self,name,number):
      #  self.add_item = name
      #  self.add_item =number
        #self.phonebook.append(item)
    #def delete_item(self,name,number):
     #   self.delete_item = name
     #   self.delete_item =number
        #for item in self.phonebook:
       #   if item.name ==name:
          #  self.phonebook.delete(name)
           # break
  #  def print_item(self,name,number):
       # self.print_item = name
      #  self.print_item =number
      #  self.phonebook.append(item) 
   # def search_item(self,name,number):
    #    self.search_item = name
     #   self.search_item =number
      #  self.phonebook.append(item)  
phonebook = {}
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class PhonebookApp:
    def __init__(self):
        self.phonebook = []

    def add_contact(self, name, number):
        contact = Contact(name, number)
        self.phonebook.append(contact)

    def delete_contact(self, name):
        for contact in self.phonebook:
            if contact.name == name:
                self.phonebook.remove(contact)
                break

    def print_contacts(self):
        print("Phonebook Contacts:")
        for contact in self.phonebook:
            print(f"{contact.name}: {contact.number}")

    def search_contact(self, name):
        for contact in self.phonebook:
            if contact.name == name:
                return contact.number
        return None

    

    

if __name__ == "__main__":
    phonebook_app = PhonebookApp()

    while True:
        print("\nPhonebook App Menu:")
        print("1. Add a Contact")
        print("2. Delete a Contact")
        print("3. Search for a Contact")
        print("4. Print All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            name = input("Enter the contact name: ")
            number = input("Enter the phone number: ")
            phonebook_app.add_contact(name, number)
        elif choice == "2":
            name = input("Enter the contact name to delete: ")
            phonebook_app.delete_contact(name)
        elif choice == "3":
            name = input()
            result = phonebook_app.search_contact(name)
            if result:
                print(f"Phone number for {name}: {result}")
            else:
                print("error.")
        elif choice == "4":
            phonebook_app.print_contacts()
     
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4/5).")

     