import logging


while True:
    try:
        valeu1 = input("entter valeu 1:")
        valeu1 = int(valeu1)
        value2 = input("entter valeu 2:")
        value2= int(value2)

        valuedivded = valeu1 / value2
        print(valuedivded)
    
    except (ZeroDivisionError, ValueError) as e:
        print("thare was zerro in value 2")
        logging.warning(e)
    except:
        print("the value entered was invalid")
    else:
        print(valuedivded)
        break
    finally:
        print("this code will always run")