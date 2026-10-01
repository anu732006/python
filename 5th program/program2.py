class Library:
    def __init__(self):
        self.book = "Python"
        self.available = True

    def borrow(self):
        if self.available:
            print("Book borrowed")
            self.available = False
        else:
            print("Book not available")

    def return_book(self):
        self.available = True
        print("Book returned")


# Create object
library = Library()

print("Book:", library.book)

library.borrow()
library.borrow()
library.return_book()