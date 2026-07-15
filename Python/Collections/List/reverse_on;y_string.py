list = ["python",10,"django",20,"AI"]

for i in str(list):

    if i.isalpha():

        list[list.index(i)] = i[::-1]

print(list)