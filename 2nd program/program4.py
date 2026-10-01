balance = 1000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Balance =", balance)

elif choice == 2:
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("New Balance =", balance)

elif choice == 3:
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance = balance - amount
        print("New Balance =", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")