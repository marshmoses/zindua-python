class School:
    def __init__(self, name, location, popln):
        self.name = name
        self.location = location
        self.popln = popln

class Child(School):
    def __init__(self, name, location, popln, Child_name, Child_age):
        super().__init__(name, location, popln)
        self.Child_name = Child_name
        self.Child_age = Child_age

# Create an instance of the School class
school = School("Jamhuri", "Ngara", 500)

# Create an instance of the Child class
child = Child("Jamhuri", "Ngara", 15, "christine", 15)
child1= Child("Jamhuri", "Ngara", 15, "John", 45)

# Access properties of the School and Child classes
print("School Name:", school.name)
print("Location:", school.location)
print("Population:", school.popln)

print("Child Name:", child.Child_name)
print("Child Age:", child.Child_age)

