

class Circle():
    radius = 0
    x = 0
    y = 0
    collor = ""
    filled = False

circles = []

for x in range(0,10):
    c = Circle()
    c.radius = int(input("Enter the circle radios: "))
    circles.append(c)


print(circles[6].radius)



