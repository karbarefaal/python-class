from random import *

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