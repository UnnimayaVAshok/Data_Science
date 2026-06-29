num = 50

n = int(input("Enter the number: "))

count = 1

while(n != num):

    print("Too low" if n < num else "Too high")

    n = int(input("Enter the number: "))

    count += 1

print(f"Well done....you took {count} attempts")