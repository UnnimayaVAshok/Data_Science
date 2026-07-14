text = "Python123ABC"
count_lower = 0
count_upper = 0
count_digit = 0
count_other = 0
for i in text:
    if i.islower():
        count_lower += 1
    elif i.isupper():
        count_upper += 1
    elif i.isdigit():
        count_digit += 1
    else:
        count_other += 1
print(f"U = {count_upper},L = {count_lower},D = {count_digit},O = {count_other}")