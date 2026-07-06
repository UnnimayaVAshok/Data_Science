text = "PyTHon123"
count_upper = 0
count_lower = 0
count_other = 0

for i in text:

    if i.isupper():

        count_upper += 1

    elif i.islower():

        count_lower += 1

    else:

        count_other += 1


print(f"{count_upper} uppercase letters and {count_lower} lowercase letters and {count_other} other")
