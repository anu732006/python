class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def show_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            print("-", book)

    def search_book(self, book):
        if book in self.books:
            print("Book found!")
        else:
            print("Book not found!")


# Create object
library = Library()

library.add_book("Python")
library.add_book("Java")

library.show_books()

library.search_book("Python")
library.search_book("C++")