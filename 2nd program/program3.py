balance = 1000

amount = int(input("Enter withdraw amount: "))

if amount <= balance:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")