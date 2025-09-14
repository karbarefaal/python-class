# r a w x
# t b
#   f.readline()

identification = {
    "name": "ali",
    "lname": "sajjadi",
    "age": 27,
}
f = open("text.txt",'wb')
f.write(str(identification).encode())
f = open("text.txt")
print(f.read())

# with open("text.txt") as f:
#     for x in f:
#         print(x)

# try:
#     f = open("text.txt","x")
# except:
#     print("You can not do this")


# import os
# if os.path.exists("text.txt"):
#     os.remove("text.txt")
# else:
#     print("The file does not exist.")

# os.rmdir("myfolder")

