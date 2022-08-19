import numbers
from typing import final


def factorial(number):
    final = 1
    for i in range(number, 0 ,-1):
        final = final * i
    return final


print( factorial(982) )


def factarialRecur(number):
    if number == 1:
        return number
    else:
        return number * factarialRecur(number - 1)
print(factarialRecur(6))
