def withdrawal(balance,amount):

    if amount > balance:

        print("Check balance")

    elif amount == balance:
        balance = 0
        print(balance)
        print("Account empty")

    else:

        balance -= amount
        print(balance)
withdrawal(5000,1200)