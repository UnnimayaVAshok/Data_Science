# wap to classify elements and count, alphabets,digit and special chars

list = ["A","5","@","b","9","#","z"]
alpha = []
digit = []
others = []
for i in list:
    if i.isalpha():

        alpha.append(i)

    elif i.isdigit():

        digit.append(i)

    else:

        others.append(i)

print(alpha,digit,others)
    

        