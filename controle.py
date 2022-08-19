
#for x in range(0, 10):
 #   print(str(x))

x = 10
y = 15

while x < y:

    print("x is: ", x)
    answer = input("press y to continue this loop. ")

    if answer == "y":
        continue

    x += 1

else:
    print("this tjhe and of the loop")
print("this the and of my code")