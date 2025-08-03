# quit_flag = False
# match quit_flag:
#     case True:
#         print("Quitting")
#     case False:
#         print("System is on")

#=======================================
# using match in function overloading

# def calc(n: int):
#     return n**2

# def calc(n: float):
#     return n**3

# n = 9.5
# is_int = True

# match is_int:
#     case True:
#         print("Square is: ", calc(n))
#     case False:
#         print("Cube is: ", calc(n))
        
#==============================================

# quit_flag = 4
# match quit_flag:
#     case True:  #        quit_flag == True
#         print("Quitting")
#     case False:
#         print("System is on")
#     case _:
#         print("Nothing")

#==================================================

# sample =False
# match sample:
#     case (True | False):
#         print('It is a boolean value')
#     case _:
#         print("Not a boolean value")

#==========================================

# list1 = ['a','b','c','d']
# match list1:
#     case ['e','f']:
#         print('e,f present')
#     case ['a','b','c','d']:
#         print('a,b,c,d present')
#     case _:
#         print('Nothing')
        
#================================================

# class Switch:
#     on = 1
#     off= 0
    
    
# status=0
# match status:
#     case Switch.on:
#         print("switch is on")
#     case Switch.off:
#         print("switch is off")
        
#======================================

# n = int(input('Enter a num: '))
# match n:
#     case n if n<0:
#         print('num is negative')
#     case n if n > 0:
#         print('num is positive')
#     case _:
#         print('num is zero')

#=========================================

# def http_error(status):
#     match status:
#         case 400:
#             return 'bad request'
#         case 404:
#             return 'Not found'
#         case 418:
#             return 'Network Down'
#         case _:
#             return 'something\'s wrong with the internet'

# a = http_error(400)
# print(a)
# print(type(a))
            
#====================================================

# def http_error(status):
#     match status:
#         case 401 | 403 | 404:
#             return 'bad request'
#         case 418:
#             return 'Network Down'
#         case _:
#             return 'something\'s wrong with the internet'

# print(http_error(400))

#=======================================================

            