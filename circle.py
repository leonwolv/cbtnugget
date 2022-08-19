import math

class Cords():
    x = 0
    y = 0

class Circle():
    pi = 3.141
    radius = 0
    x = 0
    y = 0
    color = ""
    filled = False
    def circumfrence(self):
        return self.radius * Circle.pi * 2
    def myfunc(self):
        print("myfunc was Invoke - radius - {self.radius}")