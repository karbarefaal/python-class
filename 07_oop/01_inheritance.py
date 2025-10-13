#======================== first session from below to up===============

class A:
    def __init__(self):
        print("class A")
class B(A):
    def __init__(self):
        print("class B")
        # super().__init__()
        A.__init__(self)

o = B()


#====================================================================

# print(isinstance(obj2, Mammals))    # True
# print(isinstance(obj2, Cat))


# print(issubclass(Dog,Animal))       # True
# print(issubclass(Mammals, Cat))


#======================================================================

class Animal:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def eat(self):
        print("I can eat")

class Mammals(Animal):
    def __init__(self,name,type,age):
        super().__init__(name,type)
        self.age = age
class Dog(Mammals):
    def __init__(self,name,type,age,breed):
        super().__init__(name,type,age)
        self.breed = breed
    def eat(self):
        print("I like to eat bones.")


class Cat(Mammals):
    def __init__(self,name,type,age,color):
        print("cat is cating")
        super().__init__(name,type,age)
        self.eye_color = color

obj1 = Animal("Pinki", "Girrafe")
obj2 = Mammals("Duka", "Bear", 4)
obj3 = Dog("Mika", "Dog", 3, "German")
obj4 = Cat("Hesam", "Cat", 1, "Persian")
print(obj1.type)
print(obj2.type)
print(obj3.type)
print(obj4.type)

#====================================================================

class Animal:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def eat(self):
        print("I can eat")

class Mammals(Animal):
    def __init__(self,name,type,age):
        super().__init__(name,type)
        self.age = age
class Dog(Mammals):
    def __init__(self,name,type,age,breed):
        super(Mammals, self).__init__(name,type)
        self.breed = breed

    def eat(self):
        print("I like to eat bones.")

obj1 = Animal("Pinki", "Cat")
obj2 = Mammals("Duka", "bear", 4)
obj3 = Dog("Mika", "Dog", 3, "German")
print(obj1.type)
print(obj2.type)
print(obj3.type)

#==========================================================

class A:
    def __init__(self):
        print("class A")

class B:
    def __init__(self):
        print("class B")

class C(A,B):
    def __init__(self):
        print("class C")
        B.__init(self)  # raveshe 1
        A.__init(self)
        super().__init__() # raveshe 2
        

obj = C()

#==============================================================

# Inheritence
class Bird:     #Super class
    def __init__(self):
        print("Bird is Ready")
    def who_is_this(self):
        print("Bird")

class Hen(Bird):    #Sub class
    def __init__(self):
        print("Hen is ready")
    def who_is_this(self):
        print("Hen")

h = Hen()
h.who_is_this()