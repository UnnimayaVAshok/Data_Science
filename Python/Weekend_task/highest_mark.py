students = {"Rahul":82,"Anu":91,"Arjun":78,"Meera":95}

highest_mark = 0

for i in students:

    if students.get(i) > highest_mark:

        highest_mark = students.get(i)
        name = i

print(name)