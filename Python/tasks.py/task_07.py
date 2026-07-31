# 6)Given a pattern text=”ABEABAIACB”**

#    Write a program to print most recursive consonant from above text** 

#    Output=B**

text="ABEABAIACB"

vowels = "aeiouAEIOU"
largest = 0
for i in text:
    if i not in vowels:
        if text.count(i) > largest:
            letter = i

print(i)
