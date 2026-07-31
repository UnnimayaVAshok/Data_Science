numbers = [9,6,1,7,8,4]

smallest = float("inf")
sec_smallest = float("inf")

for i in numbers:

    if i < smallest:
        sec_smallest = smallest
        smallest = i
    elif i > smallest and i < sec_smallest:

        sec_smallest = i
        

print(sec_smallest)

"""
random()
json()
python database connectivity
sqlite3
bitwise operators

"""