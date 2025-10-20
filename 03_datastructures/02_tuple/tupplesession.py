tup = ("ali", "saeed", "kasra", "mehdi")
# immutable
tup.count()
tup.index()
sorted(tup)
reversed(tup)



#===========================================================

# review list comprehension

# l = [i ** 2 for i in range(1,11)]
# print(l)

#===================Tuple========================

# tup = (1,"hello",True,"salam",'reza','mahsa')
# print(type(tup))
# print(tup[1])

# tup2 =  1, "hi",True

# # print(type(tup2))

#============unpacking tuple============================

# a,*_,c = tup
# a = tup[0]
# c = tup[len(tup) - 1]
# print(f"you're index {len(tup) - 1} is {c}")

# print(type(b))
# tup[1] = 'bye'
# print(tup)

#=================variety of costum strings=======================

# print(f'a is {a} and b is {b} and c is {c}')
# print('a is %i and b is %s and c is %s' % (a,b,c))
# res = 'a is {} and b is {}  and c is {}'.format(a,b,c)
# print(res)

# print(len(tup))

#=============================================================

# names = ('ali','mehdi','kasra','ali')
# contact_ways = ('ali@gmail.com',[1,2,3],'kasra@gmail.com')
# # names = names + contact_ways
# names += contact_ways
# print(names)
# names[5][2] = 5
# print(type(names[5]))


#================================================


student_profile = ('sara', 18,      (True,['math', 'history', 'geography'])        )
student_profile[2][1][1] = 'chemistry'
print(student_profile[2][1][0])

# shallow copy 
student_profile2 = student_profile[:]

from copy import copy,deepcopy

st2 = copy(student_profile)
# print(id(student_profile))
# print(id(st2))
# print(id(student_profile[0]))
# print(id(st2[0]))

# deepcopy

# st_deep = deepcopy(student_profile)
# print(id(student_profile))
# print(id(st2))
# print(id(student_profile[0]))
# print(id(st2[0]))

#======================================================
# concatenation, repetition

# print(3 * student_profile)


#===================================================
#reversed sorted
a = (1,2,3,99,-34,8,1,2,1)
print(tuple(reversed(a)))
print(sorted(a ,reverse=True),)

b = (('ali','sajjadi'),('kasra', 'daneshvar'))
print(sorted(b , key=lambda b: b[1]))

print(a.count(1))
print(a.index(99))


print(min(a))
print(max(a))
print(len(a))



#=========
# in
# not in


# tuple()    type casting

#==========================================

#===========tuple using in a specific index name as a object====
# from collections import namedtuple

# person = namedtuple("Person",('name', 'family'))
# ali = person('ali','sajjadi')
# print(ali.name)

#==========================not important======================
class Person :
    
    def __init__(self, name, family):
            self.name = name
            self.family = family  
            
    def myFunc(self):
        print('Done!')
        
        
object1 = Person('mehdi','ghasemi')
print(object1.name)
object1.myFunc()
            

