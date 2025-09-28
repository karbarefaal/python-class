#============================second session================================

class MyNewClass():
    """
    This is a Docstring for MyNewClass
    """
    def __init__(self,name,family):
        self.name = name
        self.family = family

    def say_hello(self):
        print(f"hello {self.name} {self.family}")

a = MyNewClass("ali", "sajjadi")
print(a.__doc__)
print(a.name, a.family)


b = MyNewClass("kasra", "daneshvar")
print(b.name, b.family)

print(f"id a is {id(a)}")
print(f"id b is {id(b)}")


# 4 principles of oop languages are encapsulation,inhertence,abstraction,polymorphism



#========================================first session ============================================================

# global variable
age = 22

# function
def walk():
    pass

class Human:

    # property
    # age = 22
    # gender = "male"
    # height = 180

    #constructor method
    def __init__(self, nameHuman, ageHuman, genderHuman, heightHuman):
        self.name = nameHuman
        self.age = ageHuman
        self.gender = genderHuman
        self.height = heightHuman

    # method
    def walk(self):
        print(f"{self.name} is walking")

    def eat(self):
        print(f"{self.name} is eating")

kasra = Human("kasra",17,"male",188)
mehdi = Human("mehdi",18,"male",180)
sara = Human("sara",20,"female",170)
print(kasra.age, mehdi.height, sara.gender,)

mehdi.walk()
kasra.eat()
