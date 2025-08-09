# def my_func(a): # parameter
#     print(f'hi {a}')

# my_func('ali')   # argument       #a <- 3
# my_func('sajjadi')


#=====================================

# def sign_up():
#     pass

# sign_up()

#======================================

# def jadval_zarb(n):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             k = i* j
#             print(k,end="  ")
#         print()
        
# jadval_zarb(20)

#===========================================


# def print_my_name():
#     return 'ali sajjadi'

# print(print_my_name())

#===============================================

# def print_my_name():
#     print('hi')

# print_my_name()

#================================================

# def print_my_name():
#     print('hi')
#     return 'hi'

# print(print_my_name().upper())

#================================================

# pinfhedt('hi')

#================================================

# 1 - required parameter
# 2 - default parameter
# 3 - keyword parameter
# 4 - multiple parameter (as you wish)

# 1 - required parameter (required arg)
# def my_site(d):
#     """
#     This function will
#     show us printing my_website
#     """
#     print(d)
    
#my_site()   #TypeError: my_site() missing 1 required positional argument
# my_site("rahemehr.ir")
# print(my_site.__doc__)
# my_site(True)

#===============================================

# shopping_list = {}
# def add_item(item_name, item_quantity):
#     if item_name in shopping_list.keys():
#         shopping_list[item_name] += item_quantity
#     else:
#         shopping_list[item_name] = item_quantity

# add_item("magnom icecream", 4)
# print(shopping_list)
# add_item("milk", 3)
# print(shopping_list)
# add_item("chessboard", 2)
# print(shopping_list)
# add_item("magnom icecream", 3)
# print(shopping_list)

#================================================

# fibonacci sequence
# present fibonacci sequence until n number
# def fib(n):
#     a,b = 0,1
#     while a < n:
#         print(a,end=" ")
#         a,b = b, a+b    # swap
# fib(20)

#==================================================

# 2 - default argument
# shopping_list = {}
# def add_item(item_name, item_quantity):
#     if item_name in shopping_list.keys():
#         shopping_list[item_name] += item_quantity
#     else:
#         shopping_list[item_name] = item_quantity
        
# add_item("bread",4)
# add_item("bread")
# print(shopping_list)

#===============================================

# 3 - keyword argument
# add_item("milk",item_quantity=10)   # after keyword arg you should use another keyword arg(s)

#==================================================

# def ask_ok(propmt,retries=4,reminder="please try again"):
#     while True:
#         ok = input(propmt)
#         if ok in ('y','ye','yes','Y','Yes','Yeah'):
#             return True
#         retries -= 1
#         if retries < 0:
#             raise ValueError('invalid user response')
        
# myVar = ask_ok('Do you really want to quit?')
# print(type(myVar))

#=========================================================

# the problem: default argument is once

# def f(a,l=[]):
#     l.append(a)
#     return l

# print(f('salam'))
# print(f('salam'))
# print(f('salam'))
# print(f('salam'))
# print(f('salam'))

#==============-> solving above problem

# def f(a, l=None):
#     if l is None:
#         l = []
#     l.append(a)
#     return l

# print(f('salam'))
# print(f('salam'))
# print(f('salam'))
# print(f('salam'))
# print(f('salam'))

#=================================

# 4 - multiple argument (as you wish)

# def personl_info(*args,**keyword):    
#     # *args -> tuple    
#     # **keyword -> dict    
#     print(keyword)
#     print(len(keyword))
#     print(args)
#     print(len(args))
    
# personl_info('salam', a = True, b = 'salam')   #keyword arg
# personl_info(True,False,"salam")

#============================================

# def rahemehr_courses(course,*args,**keywords):
#     print("--Do you have any", course,"course?")
#     print('--I\'m sorry, we don\'t have',course,"course.")
#     for arg in args:
#         print(arg)
#     print('-' * 40)
#     # print(keyword)
#     for kw in keywords:
#         print(kw,":",keywords[kw])
        
# rahemehr_courses(
#     'java',
#     'I love to learn Golang',
#     'I love to learn Database',
#     secretary = "Sima bina"  ,  
#     Client = "Ramin"
# )
        
#================================================

# some_items = ('coffee','tea','cake','soda')
# print(*some_items)  # unpacking

#===============================================

# def rahemehr_courses(*arguments,**keywords):
#     print(arguments)
#     print(keywords)

# rahemehr_courses(*[2,3,4,5,66])
# rahemehr_courses(**{'a': 22,'b':33})

#================================================

# python 3.8    
# /  after parameter ->  not allow to use keyword argument   
# * before parameter ->  You have to use keyword argument
# print(help(float))

# print(float(10))

# def incr(x , /):
#     return x + 1
# print(incr(10))  

#==============================

# def greet(name,/, greeting='hello'):
#     return f'{greeting}, {name}'

# print(greet("kasra",'hi'))
# print(greet("Ali"))

#============================================

# def to_fahrenheit(* , celsius):
#     return 32 + celsius * 9 / 5

# print(to_fahrenheit(celsius=30))

#============================================

# def headline(text, / , border = '^',*, width=50):
#     return f'{text}'.center(width,border)

# print(headline(' Hele dan ',"3"))

#===========================================

def my_func(a: int) -> int:
    return a

my_func(True)
my_func(3.14)
my_func('salam')

name:str = "ali"

#===========================================



















