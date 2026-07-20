# print 1st non repeating element in a list

list_1 = [2,3,4,2,3,5,6]

for i in list_1:

    if list_1.count(i) == 1:

        print(i)
        break