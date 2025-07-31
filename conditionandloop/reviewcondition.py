# if for switch while

# if (expression):
    # statement
    
# n = 4
# if n > 5:       
#     print("Hey!")
# elif n == 5:
#     print('mirshekari')
# elif n == 3:
#     print('gooli')
# else:
#     print('finally me')
    
# print('hello world')


#===================================

# if 4 >3: print('hi'); print('bye')

# turnary operator
# raining = False
# print('Let\'s go to the','beach' if not raining else 'library')

# raining = True
# print('Let\'s go to the','beach' if not raining else 'library')

# age = 12
# s = 'minor' if age < 21 else 'adult'

# p = [1,2,3,4]
# s = [i**2 for i in p if True]
# print(s)

#=============

# x = 10
# if x > 5:
#     if x > 8:
#         print('not yet')
#         if x == 10:
#             print('you win')
#         else:
#             print('x is ', x)
#     else:
#         print('mio')
# else:
#     print("bashe")

#=======================================

# x = 3
# s = (
#     "foo"
#     if x == 1
#     else "bar"
#     if x == 2
#     else "baz"
#     if x == 3
#     else "bye"
#     if x == 4
#     else "mirshekari"
# )
# print(s)

#=====================================

# x = 5
# y = 0
# if x < y:
#     print('x < y is yes')
# if x > y:
#     print('x > y is yes')
# if x:
#     print('x is yes')
# if y:
#     print('y is yes')
# if x or y:
#     print(x or y)
# if x and y:
#     print(x and y)
# if 'aul' in 'grault':
#     print('aul is exist')
# if 'quux' in ['foo','bar','baz']:
#     print('quux is exist')
    

#=======================================
# while -> loop

# while expression:
#   statement


# n = 1000
# while n > 0:
#     n -= 1
#     print(n)
# print('Done!')

#=======================================

# a = ['foo','bar','baz']
# while a:
#     print(a.pop())

#===================================================

# n, sum, i = 10, 0 ,1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

#========================================================

# n = 3
# while n > 0:
#     n -= 1
#     if n == 2:
#         break
#     print(n)
# print('loop ended')

#===================================================
# n = 4
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n)
# print('loop ended!')

#==============================================

# a = 0
# while a == 0:
#     num = int(input('enter a number'))
#     print('You entered', num)
#     if num == 0:
#         break
# print('good bye!')

#==========================================
# n = 5
# while n > 0: 
#     n-=1
#     print(n)
    

#========================================

# i = 0
# while i < 10:
#     i += 1
#     j = 0
#     while j < 10:
#         j += 1
#         print(i*j,end='\t')
#     print()
        
#========================================================

# your exercise 1: print the below asterixs on the console

#   *
#   **
#   ***
#   ****

# your exercise 2: print the below asterixs on the console

#   ****
#   ***
#   **
#   *