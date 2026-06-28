balance = int(input("Enter the balance: "))

withdrawal_amount = int(input("Enter the amount to withdraw: "))

if withdrawal_amount <= 0:

    print("Invalid amount")

elif balance == 0:

    print("Account empty")

elif withdrawal_amount > balance:

    print("Insufficient balance")

elif withdrawal_amount == balance:

    print("Account will become empty")

else:

    balance -= withdrawal_amount

    print(f"Transaction successfull....available balance {balance}")