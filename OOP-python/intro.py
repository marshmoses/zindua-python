class Person:
    def __init__(self, name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def greet(self):
    
        print("Hello my name is " + self.name) 
           
myPerson= Person('Jack' , 76 ,'Lab Technician' )  
    

print(myPerson.name)

print(myPerson.age)

print(myPerson.occupation)

