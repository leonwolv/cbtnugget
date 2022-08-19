


studentGrades = {"Ben": 92, "Diane": 97, "Sam": 81}


print(studentGrades["Diane"])

myCar = ({"Make": "Ford", "model": "Model A", "Year": 2031},
{"Make": "Chevy", "model": "Cavalier", "Year": 1997})

print(myCar[1]["model"])

for item in studentGrades:
    print(studentGrades[item])

if 92 in studentGrades:
    print("It is!")

if 92 in studentGrades.values():
    print("It is")

valeus = studentGrades.values()
valeuslist = list(valeus)
print(valeuslist[1])

keys = studentGrades.keys()
keylist = list(keys)
print(keylist)



for i in range(0,len(valeus)):
    print(studentGrades[keylist[i]])


items = studentGrades.items()

print(items)

itemlist = list(items)

print(itemlist[0][0])



