list = ["Python", "java", "PYTHON", "Java", "C", "c"]

new = []

for i in list:
    if i.lower() not in new:
        new.append(i.lower())

print(new)