# i = 0
# n = 4
# while i < n:
#     i += 1
#     j = 0
#     while j < n - i + 1:
#         j += 1
#         print('*',end='')
#     print()
        
    
        
# a = 0
# while a< 100:
#     a += 1
#     print(a+1,'sorry')



# mylist = ['salam','man', 'ali','hastam']
# a = 0
# while a < len(mylist):
#     print(mylist[a])
#     a += 1
    
    
    
# for item in mylist:
#     print(item)
 
 
 
# mylist = ['salam','man', 'ali','hastam']
# mystr = ''
# for item in mylist:
#     mystr += item + ' '
# print(mystr)



# a = 'rahemehr.ir'
# for b in a:
#     print(b)
   
    
# words = ['cat', 'window', 'dog']
# for w in words:
#     print(w, len(w))
    
    
    
# numbers = [32,66,17,64]
# sum = 0
# for i in numbers:
#     sum += i
# print(sum)



# x = range(10)
# for i in x:
#     print(i**2)
# print(x)
# print(type(x))
# print(list(x))

# print(list(range(4,8)))
# print(list(range(8)))
# print(list(range(4,90,4)))


# singer = ['ebi','mahasti', 'vigen', 'daryoush']
# for i in range(len(singer)):
#     print(f'sadaye {singer[i]} zibast.')
    
    
    
# singer = ['ebi','mahasti', 'vigen', 'daryoush']
# i = 0
# while i < len(singer):
#     print(f'sadaye {singer[i]} zibast.')
#     i += 1
 
    
# singer = ['ebi','mahasti', 'vigen', 'daryoush']
# for i in singer:
#     print(f'sadaye {i} zibast.')


# for i in ['foo','bar','baz','qux']:
#     if 'b' in i:
#         continue            # or break
    # print(i)
    

# num = [0,1,5,6]
# for i in num:
#     print(i)
# else:
#     print('dge adad nist bor khoneton')
    

# student_name = "Nadar"
# marks= {
#     'Mehdi': 30,
#     'Kasra': 38,
#     'Ali': 40,
#     'Nadar': 42,
#     'Samira': 50
# }

# for st in marks:
#     if (student_name == st):
#         print(f'Jenab {st} shomareh shoma {marks[st]} ast')
#         break       # continue
#     else:
#         print(f'No entry with that name found. our key was {st}')
        

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
#     # Output:
#     # name: Alice
#     # age: 30
#     # city: New York


# list_1 = ['apple','banaba','orange','mango']
# for index in range(len(list_1)):
#     print(index,list_1[index])
    
# list_1 = ['apple','banaba','orange','mango']
# # it's better to use enumerate
# x = list(enumerate(list_1))
# print(x)
# for index,element in x:
#     print(index,element)
    
#==============================================

# jadval zarb

# with while      
# i = 0
# while i < 10:
#     i += 1
#     j = 0
#     while j < 10:
#         j += 1
#         print(i*j,end='\t')
#     print() 
    

#with for in    
# for i in range(1,11):
#     for j in range(1,11):
#         k = i* j
#         print(k,end="\t")
#     print()


#=======================================================================

# while True:
#     number = int(input('please enter a positive number: '))
#     print(number)
#     if number <= 0:
#         break
    
# print('our app is closed.')
    
    
#============================
# from random import randint
# LOW = 1
# HIGH =100
# num = randint(LOW,HIGH+1)
# while True:
#     myGuess = int(input('Please enter a number: '))
#     if myGuess == num:
#         print(f'You found it. your number was {num}')
#         break
#     elif(myGuess > num):
#         print('Please enter a smaller number')
#     else:
#         print('Please enter a bigger number')
        
#========================================

a = 0
n = 5
nums= []
x = None

while(a < n):
    a += 1
    x = int(input(f'Please Enter your number {a}: '))
    nums.append(x)
    
print(max(nums))
# print(max.__doc__)


#=====================================================================



    