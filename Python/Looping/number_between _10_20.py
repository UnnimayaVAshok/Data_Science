num = int(input("Enter a number between 10 and 20: "))

while(num <= 10 or num >= 20):

    print("Too low" if num <= 10 else "Too high")

    num = int(input("Enter a number between 10 and 20: "))

print("Thank you")