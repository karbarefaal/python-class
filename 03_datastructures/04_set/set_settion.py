# a = {1,1,1,2,1,[1,2,3],"salam", (1,)}
# print(a)


# my_set = set([1,3,"salam",(1,2,3)])
# print(my_set)

# my_set.add(5)
# my_set.update([1,2,3,4,5,6,7])
# print(my_set)

# my_set.discard("hihi")
# print(my_set)
# my_set.remove(4)
# print(my_set)

# my_set.pop()
# my_set.clear()
# del my_set
# print(my_set)

#=========================================

a = {1,2,3}
b = {3,4,5}
print(a | b)
print(a.union(b))

print(a & b)
print(a.intersection(b))

print(a-b)
print(b-a)
print(a.difference(b))


print(a ^ b)
print(a.symmetric_difference(b))

#=================================


x = frozenset(['pizza', 'mushroom', 'burger'])
print(type(x))
# print(x.add())   Neeeeeeeeeeeeeeeeeees=miiiiiiiiiiiishhhhhheeeeeehhhh

f = frozenset([1,2,3,4])
print(id(f))
f = x | f
print(id(f))
print(f)





