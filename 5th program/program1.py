# Library Management System using OOP

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.book_id, "-", self.title, "-", self.author, "-", status)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        print("\n===== BOOK LIST =====")
        for book in self.books:
            book.display()

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


# Create Library object
library = Library()

# Add books
library.add_book(Book(1, "Python Programming", "Guido van Rossum"))
library.add_book(Book(2, "Data Structures", "Mark Allen"))
library.add_book(Book(3, "Web Technology", "John Smith"))

# Menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id)

    elif choice == "3":
        book_id = int(input("Enter Book ID to return: "))
        library.return_book(book_id)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")