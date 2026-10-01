balance = 1000

print("===== ATM =====")
print("1. Check Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your Balance is:", balance)
else:
    print("Invalid Choice")