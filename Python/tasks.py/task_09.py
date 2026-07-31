# 8)wap to print the characters of a string in even positions. >>>      name= "python"    o/p = y h n**

text = input("Enter the string: ")

for i in range(len(text)):

    if i % 2 != 0:

        print(text[i],end = " ")