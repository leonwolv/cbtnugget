

from logging import exception


value1 = input("entter valeu 1:")
valeu2 = input("entter valeu 2:")


assert(valeu2 != "0"), "valeu 2 can't be a zero"
#if valeu2 == "0":
 #   raise exception("valeu 2 can't be a zero")
value1 = int(value1)
valeu2= int(valeu2)
print( value1 / valeu2)