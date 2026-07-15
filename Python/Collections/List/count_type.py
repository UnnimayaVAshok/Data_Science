# wap to classify elements and count, alphabets,digit and special chars

list = ["A","5","@","b","9","#","z"]
count_alpha = 0
count_digit = 0
count_others = 0
for i in list:
    if i.isalpha():

        count_alpha +=1

    elif i.isdigit():

        count_digit += 1

    else:

        count_others += 1

print(count_alpha,count_digit,count_others)
    

        