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
