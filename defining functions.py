import time

def greetUser(name):
    if time.localtime().tm_hour < 12:
        print(f"goedmorning {name}")
    else:
        print(f"Good afternoon {name}")


greetUser("Ben")
greetUser("Diane")

def isVowel(value,pos = 1):
    if len(value) < pos:
        return "string is to short"
    elif value[pos-1] in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        return f"the value in position {pos} is a vowel"
    else:
        return f"the value in position {pos} is not A vawel."
print(isVowel("Ben", 2))