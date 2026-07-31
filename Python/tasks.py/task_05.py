# 4)Write a function that capitalizes the first and fourth letters of a name



def caps(text):
    new = ""
    for i in range(len(text)):
        
        if i == 0 or i == 3:
            
            new += text[i].upper()
        else:
            new += text[i]

    return new

print(caps("helloo"))