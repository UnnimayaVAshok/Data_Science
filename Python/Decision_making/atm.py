balance = int(input("Enter the balance: "))

print(f"1) Check balance \n2) Deposit \n3) Withdraw amount \n4)Exit")

choice = input("Enter your choice: ")

if choice =="1":

    print(f"Your balance is {balance}")

elif choice =="2":

    deposit_amount = int(input("Enter the amount to be deposited: "))

    balance += deposit_amount

    print(f"Amount deposited successfully and your current balance is {balance}")

elif choice =="3":

    withdraw_amount = int(input("Enter the amount to withdraw: "))

    if withdraw_amount > balance:

        print(f"Sorry...Insufficient bank balance")

    elif balance - withdraw_amount < 1000:

        print("Can't maintain minimum balance")
    
    else:

        balance -= withdraw_amount

        print(f"Transaction successfull and your current balance is {balance}")
    
elif choice == "4":

    print(f"Thank You")

else:

    print(f"Get out")