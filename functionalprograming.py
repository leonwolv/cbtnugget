import functools


from logging import Filterer


numbers = [1,2,3,4,5]
#squared = []

#def sequareMe(n):
#    return n ** 2

squared = map(lambda x: x ** 2, numbers)

squared = list(squared)

print(squared)


numbers = [1,2,3,4,5,9,10,14,13,15,16,17,20]

Filtered = filter(lambda x: x >= 19 , numbers)

Filtered = list(Filtered)

print(Filtered)


reduced = functools.reduce(lambda x,y: x+y, numbers)

print(reduced)

