def second_largest():
    n = int(input("Enter how many numbers: "))

    largest = int(input("Enter number: "))
    second = largest

    for i in range(n - 1):
        num = int(input("Enter number: "))

        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    print("Second largest =", second)
    return second

print(second_largest())
