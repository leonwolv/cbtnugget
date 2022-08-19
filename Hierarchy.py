import logging
import sys

while True:
    try:
        valeu1 = input("entter valeu 1:")
        valeu1 = int(valeu1)
        value2 = input("entter valeu 2:")
        value2= int(value2)

        valuedivded = valeu1 / value2
        print(valuedivded)
    
    except ArithmeticError:
        print("thare was Arithmetic Error")
    except ValueError as e:
        print("Plaese entere a valid number")
    except Exception as e:
        print(e)
        print("the value entered was invalid")
