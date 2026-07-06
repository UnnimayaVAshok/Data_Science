# wap to get the count of uppercase letters and lowercase from the string below

# text = "ProGraMMinGLanGUAge"

text = "ProGraMMinGLanGUAge"

count_upper = 0

count_lower = 0

for i in text:

    if i.isupper():

        count_upper += 1

    else:

        count_lower += 1

print(f"{count_upper} uppercase letters and {count_lower} lowercase letters")
