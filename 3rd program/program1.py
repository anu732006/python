password = input("Enter password: ")

# Password validation
if len(password) >= 6:
    print("Password is valid")

    # Simple encryption
    encrypted = ""
    for ch in password:
        encrypted = encrypted + chr(ord(ch) + 3)

    print("Encrypted Password:", encrypted)
else:
    print("Password is invalid")
    print("Password must contain at least 6 characters")