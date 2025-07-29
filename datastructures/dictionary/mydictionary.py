# my_dict = {}
# print(type(my_dict)) -> dict

# my_dict = {1:"apple", 20: ["ball","wall","gal"]}
# print(my_dict[20])



# my_dict2 = {3: "student", 4: "book"}

# my_dict = {"Name": "Mehdi","Age": 18,"Salary": 10000, "Sport": "Handball"}
# my_dict["BandScore"] = 7
# print(my_dict)


# print(my_dict["Hobby"])     # -> returns KeyError
# print(my_dict.get("Hobby"))  # -> if it doesn't exist returns None


# updating Value
# my_dict["Name"] = "Parviz"
# print(my_dict["Name"])


#============================================================



# person = {}

# person["Name"] = "Ali"
# print(person)
# person["Age"] = 18
# print(person)


# person["Spouse"] = "Angelina"
# print(person)

# person["Children"] = ["Mahsa", "Javad", "Sepehr"]
# print(person)

# person["pets"] = {"cat": "hasan", "dog": ["tomi","jabbar"]}


# print(person["Children"][1])
# print(person["pets"]["dog"])


# print(person)
# person.pop("Age")
# print(person)

# person.clear()
# print(person)

# del person


#===============================
# b = {"a": 1, "a": "blue", "a" : 3}
# print(b)


# a = {"name": 1,"age": 2}
# print(f'your value is {a["age"]}')

# print(len(a))
# print(type(a))
#=======================================


# c = {}
# c = c.fromkeys([1,2,3])
# print(c)

# c = c.fromkeys([1,2,3],"hi")
# print(c)

# d = {}
# a = "name","age","salary"
# d = d.fromkeys(a,"♣")
# # print(d)
# c.update(d) # merging two dictionaries
# print(c)

# print(list(c.values()))
# print(list(c.keys()))

#==============================================


# people ={
#     1: {"name": "Hooshang", "age":20, "job": "Developer"},
#     2: {"name": "SeyedEbrahim", "age":60, "job": "President"}
# }
# print(people[2]["age"])
# people[3]= {}
# people[3]["name"] = "Parham"
# people[3]["Job"] = "Chess Player"
# print(people)

#==========================================


# pycon = {2016: "portland", 2018: "cleveland"}
# europython = {2017:"Rimini", 2018:"Edinburgh", 2019: "Basel"}

# Method 1
# new_dict = {**pycon, **europython}
# print(new_dict)

# Method 2
# merged = pycon.copy()
# for key, value in europython.items():
#     merged[key] = value
# print(merged)

# Method 3
# (merged :=  pycon.copy()).update(europython)  #walrus
# print(merged)
# print(pycon)
# print(europython)


#=============2 sign had added in python version 3.9=======================

# print(pycon | europython)  # to merge

# pycon |= europython   # to update 2 dicts
# print(pycon)


#=========================================================

# from collections import defaultdict
# def def_value():
#     return "Not present"
# sample_dict = defaultdict("Not present")
# sample_dict['a'] = 1
# sample_dict['b'] = 2
# print(sample_dict['a'])
# print(sample_dict['b'])
# print(sample_dict['c'])

#=======================================================

from collections import UserDict
d = {"a": 1, "b": 2}
a = UserDict(d)
print(a)




 