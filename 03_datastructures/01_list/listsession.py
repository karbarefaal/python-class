my_list = []
my_list.append()
my_list.clear()
my_list.copy()
my_list.count()
my_list.extend()
my_list.index()
my_list.insert()
my_list.pop()
my_list.remove()
my_list.reverse()
my_list.sort()

#================================second session============================

# myList = [10,20,30,40,50]

# myList.append('salam')

# myList.insert(2,'bye')
# print(myList)
# print(id(myList))

# print('myList len is',len(myList))

# myList.clear()
# print(myList)

# del myList[0:1]
# print(myList)

# print(myList.pop())
# print(myList)
# print(myList.index(30))
# karbar = int(input('please remove something: '))
# myList.pop(myList.index(karbar))

# myList = [10,20,30,40,50]

# print(myList[5])

# myList.extend([70,80,90])
# print(myList)

# myList[len(myList):] = 14
# print(myList)

# myList[2:2] = [77,88,99]  # inserting a list (increasing the size of list)
# print(myList)


# # myList[1:4] = [1,1,1,1,1,1,1,1,1,1,1]  # decreasing a list (increasing the size of list)
# print(myList)
# myList.remove(88)
# print(myList)



#============================copy===========================
# aliasing   -   shallow copy    -    deep copy

myList = [10,20,30,40,50]
print(id(myList))

#  aliasing
myList2 = myList
print('our answer is: ',myList2 is myList)

# print(id(myList) == id(myList2))
# print(id(myList[0])  ==  id(myList2[0]))

# myList2[0] = 100

# print(id(myList) == id(myList2))
# print(id(myList[0])  ==  id(myList2[0]))

#shallow copy   first way
# countries = ['us', 'germany', 'uk', 'france', 'zimbabwe', 'timor leste']
# nations = countries[:]

# print(id(countries) == id(nations))
# print(id(countries[1])  ==  id(nations[1]))

# nations[2] = 'United Kingdom'

# print(id(countries) == id(nations))
# print(id(countries[2])  ==  id(nations[2]))

# shallow copy second way 
countries = ['us', 'germany', 'uk', 'france', 'zimbabwe', 'timor leste']
nations = countries.copy()   # list method

# print(id(countries) == id(nations))
# print(id(countries[1])  ==  id(nations[1]))

# nations[2] = 'United Kingdom'

# print(id(countries) == id(nations))
# print(id(countries[2])  ==  id(nations[2]))

# shallow copy third way
from copy import copy

countries = ['us', 'germany', 'uk', 'france', 'zimbabwe', 'timor leste']
nations = copy(countries)

print(id(countries) == id(nations))
print(id(countries[1])  ==  id(nations[1]))

nations[2] = 'United Kingdom'

print(id(countries) == id(nations))
print(id(countries[2])  ==  id(nations[2]))

# deep copy
from copy import deepcopy


matrix = [[1,2,3],[4,5,6]]
# print(matrix[1][1])
matrix_copy = deepcopy(matrix)

print(id(matrix)  ==  id(matrix_copy))
print(id(matrix[0])  ==  id(matrix_copy[0]))

#======================reverse=========================
# yourList = [13,77,23,2,978,324,38,'salam',True]
# print(yourList)
# print(list(reversed(yourList)))
# print(yourList)


# yourList.reverse()
# print(yourList)

yourList = [13,77,23,2,978,324,38,]
ourList = ['ali', 'mEhdi', 'mEhRan', 'Kasra']


print(min(yourList))
print(max(yourList))

print(min(ourList))
print(max(ourList))

print('ali' not in ourList)

# print(sorted(ourList))
# print(ourList)

# yourList.sort()
# print(yourList)

theirList = ['ali','mehdi', 'ali' , 'hasan', 'kasra' , 'ladan', 'parviz','mehdi', 'mehdi', ]
print(theirList.count('mehdi'))

print(['ali','mehdi', 'ali']  >  ['ali','mehdi', 'ali','Mehdi',] )

# customization for list in next sessions after inheritance




#=========================first session====================================
#===============first way to difine a variable list=====(using square bracket )=========
colors = ['red', 'pink', 'gray', 'purple', 'yellow' ,]
a= [23 ,  True   ,  colors,  (23,11), {"ali": "red","reza": "blue"}]
print(a[2][3])

#===============second way to difine a variable list===(list constructor)================
p = list('salam')
print(p)
#===============third way to difine a variable list======(list comprehension)=================================
#a  = [expression(item) for  item in iterable]    # list comprehension
myList = [number ** 2 if number % 2 == 0 else 0 for number in range(1,11) ]

#===========================old way without list comprehension =====using loop block=======================
squares = []
for i in range(11):
    squares.append(i)
print(squares)

#==================================example============================================
b = ['sang','kaghaz', 'gheychi']
for i in b:
    print(i)
print('Done!')

#==============================walrus================================================
# walrus is ( :=  ) syntax that you assign an expression in a variable 
# and simultanously you can assess the value
b = ['sang','kaghaz', 'gheychi']
if (a := b[2]) == 'gheychi':
    print('We can do it')
else:
    print('We can\'t do it')
    
#==================================example============================================
senteces = 'the rocket came back from mars'
vowels = [i for i in senteces if i in 'aeoui']
print(vowels)

#==================================example============================================
original_price = [1.25, -9.45, 10.22,22.67,-5.34]
price = [i if i > 0 else 0 for i in original_price]
print(price)

#==================================example============================================
from random import *

def get_weather_data():
    return random.randrange(90,110)

hot_items = [temp for _ in range(20) if(temp := get_weather_data()) > 100]
print(hot_items)

#=================================exercise============================================
chess_pieces=["pawn", "knight","bishop","rook","queen","king"]
my_selected_pieces= [x for x in chess_pieces if len(x) > 4]
print(my_selected_pieces) 

#=============================append=====insert=========================================
pieces = ['pawn', 'king', 'knight', 'bishop', 'queen', 'rook'] 
pieces.append('minister')
pieces.insert(3,'president')
print(pieces)