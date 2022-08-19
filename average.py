import fileinput

total = 0
studentGrades = {}

for line in fileinput.input():
    values = line.strip()
    values = line.split(",")

    studentGrades.update({ values[0] : int(values[1]) })


print(studentGrades)


for student in studentGrades:
    total = total + studentGrades[student]

average = total / len(studentGrades)
print(average)