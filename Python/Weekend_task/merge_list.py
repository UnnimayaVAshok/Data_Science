# merge 2 lists without duplicates

list_1 = [1,2,3,4,5]

list_2 = [4,5,6,7,8,9]

list_3 = list_1 + list_2

new = []

for i in list_3:

    if i not in new:
        
        new.append(i)

print(new)

