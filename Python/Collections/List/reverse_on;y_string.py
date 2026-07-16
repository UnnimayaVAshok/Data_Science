items = ["python",10,"django",20,"AI"]

for i in items:
    if type(i) == str:

        items[items.index(i)] = i[::-1]

print(items)