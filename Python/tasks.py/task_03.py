# 3)Write a Python program that takes a string input from the user."hellopython"**

# 	Find the first occurrence of the character 'o' in the string.**

# 	Swap all characters before this first occurrence of 'o' in pairs.**

# 	Leave the rest of the string unchanged.**

# &#x20;      

#         "llehopython"**

text = input("Enter a string: ")

index = text.index("o")
new = ""
for i in text:
    if i == "o":
        new += text[index-1::-1]
        break
new += text[index:len(text):]
print(new)