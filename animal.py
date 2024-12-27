class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")



my_dog = Dog("Rex", "SuperDog") 
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()



class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def say_hello(self):
        print(f"Hello, my name is {self.fname} {self.lname}")



class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)
print(f"My name is {x.fname} {x.lname} and I graduated in {x.graduationyear}")