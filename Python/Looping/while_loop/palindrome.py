n = int(input("Enter the number: "))

temp = n

reversed = 0

while(n > 0):

    digit = n % 10

    reversed = reversed * 10 + digit

    n //= 10

print("Palindrome" if temp == reversed else "Not palindrome")