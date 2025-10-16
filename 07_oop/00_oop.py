

#============================slots========================================

class Student:
    __slots__ =("name","age")
    
    def __init__(self,name,age):
        self.name = name
        self.age =age

obj1 = Student("Kasra", 17)
obj1.lastName = "Danshvar"
print(obj1.lastName)
print(obj1.__dict__) # show a obj as a dictionary
    
obj1.grade = 18
print(obj1.grade)

#========================================================================
class BankAccount:
    def __init__(self, b: float, owner: str):
        self.balance = b
        self.owner = owner

    def open_account(name: str):
        new_account = BankAccount(0,name)
        return new_account
    
    def deposit_money_on_account(account,amount: int):
        account.balance += amount

    def info(self):
        print(f"{self.owner} has {self.balance} dollar")

saman_account = BankAccount.open_account("Leonardo Decaprio")
mellat_account = BankAccount.open_account("Leonardo Decaprio")
refah_account = BankAccount.open_account("Angelina Julie")
BankAccount.deposit_money_on_account(saman_account,100)
refah_account.info()

#================================================================

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []
    def add_trick(self,trick):
        self.tricks.append(trick)
dog1 = Dog("Fido")
dog2 = Dog("Mika")
dog1.add_trick("Roll over")
dog2.add_trick("Play dead")
print(dog1.tricks)
print(dog2.tricks)

#===================Fourth session================================

class Human:
    """
    This is Human class
    """
    num_of_obj = 0
    def __init__(self,job,age,name,telephone):
        self.job = job
        self.age = age
        self.name = name
        self.tel = telephone
        self.email = name+"@rahemehr.ir"
        Human.num_of_obj += 1

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Job: {self.job}")

inputName = input("please enter your name: ")
inputJob = input("Please enter your job: ")
inputAge = int(input("please enter your age: "))
inputPhone = input("please enter your phone: ")
h1 = Human(inputJob, inputAge, inputName,inputPhone)
print(f"Dear {h1.name}. we sent a SMS on your phone.")
print(h1.name)
print(h1.email)
print(Human.num_of_obj)
h2 = Human("a",22,"a","09")
print(Human.num_of_obj)


#===========================third session===================

class Book:
    """
    This class is about Book
    """
    def __init__ (self, title, author, published_at):
        self.title = title
        self.author = author
        self.published_at = published_at

    def infoBook(self):
        show = f"""the book name is {self.title} and the author of the book
is {self.author} and also this book was published at {self.published_at}"""
        print(show)

    def __str__(self):
        return f"""
Book title: {self.title} - 
Author: {self.author} - 
Published at: {self.published_at}
"""
    
    def book_list(my_list: list):
        strList = []
        for i in my_list:
            strList.append(str(i))
        return strList
        # return [str(book) for book in my_list]    # second way

   

b1 = Book("Harry potter", "J. K. Rowling", 1997)
b2 = Book("shahnameh", "ferdosi", 400)
b3 = Book("leili va majnoon", "nezami", 500)
# print(b1.title)
# print(b1.author)
# print(b1.published_at)
# print(b2.title)
# print(b2.author)
# print(b2.published_at)
# print(b3.title)
# print(b3.author)
# print(b3.published_at)


# b1.infoBook()
bookList = [b1,b2,b3]

print(Book.book_list(bookList))

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


