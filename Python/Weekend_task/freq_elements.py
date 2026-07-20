# print frequency of every element in a list

list_1 = [2,3,2,4,3,2]

new = []

list_2 = []

for i in list_1:
    
    if i not in list_2:
        
        freq = list_1.count(i)

        new.append([i,freq])

        list_2.append(i)

print(new)