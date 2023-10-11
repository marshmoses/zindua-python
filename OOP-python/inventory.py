import csv
class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

#create ims class
class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []
#add item(user gets to append new itemto ims as II)
    def add_item(self, name, quantity, price):
        item = InventoryItem(name, quantity, price)
        self.inventory.append(item)
#remove,,,,
    def remove_item(self, name):
        self.inventory = [item for item in self.inventory if item.name != name]
#update,,,,
    def update_item(self, name, quantity=None, price=None):
        for item in self.inventory:
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price
#display ciode
    def display_inventory(self):
        for item in self.inventory:
            print(f"Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}")
#loading from csv files
    def load_inventory_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, quantity, price = row
                self.add_item(name, int(quantity), float(price))

    def save_inventory_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for item in self.inventory:
                writer.writerow([item.name, item.quantity, item.price])
if __name__ == "__main__":
    ims = InventoryManagementSystem()

    # Add products
    ims.add_item("books", 100, 25)
    ims.add_item("pens", 200, 10)
    ims.add_item("boards", 20, 1000)
    ims.add_item("cars", 5, 1000000)
    ims.add_item("buses", 2, 5000000)


    

    # Display inventory
    ims.display_inventory()

    # Update item quantity and price
    ims.update_item("books", quantity=300, price=30)
    ims.update_item("cars", quantity=30, price=300000)

    # Remove an item
    ims.remove_item("pens")
    ims.remove_item("buses")

    # Save 
    ims.save_inventory_to_csv("inventory.csv")

    # Load inventory 
    ims.load_inventory_from_csv("inventory.csv")

    # updated inventory
    ims.display_inventory()
