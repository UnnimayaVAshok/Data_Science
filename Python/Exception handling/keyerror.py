# wap to access a missing dictionary key and handle the key error

elements = {"name":"arun","age":23,"palce":"kochi"}

key = input("Enter the key: ")

try:

    print(elements[key])

except KeyError:

    print("Enter a valid key")

finally:

    print("Thank you")