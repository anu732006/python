contacts = [
    {"name": "Rahul"},
    {"name": "Priya"},
    {"name": "Arun"}
]

name = input("Enter name to delete: ")

for contact in contacts:
    if contact["name"] == name:
        contacts.remove(contact)
        print("Contact deleted!")
        break
else:
    print("Contact not found!")

print(contacts)