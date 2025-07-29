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



#
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