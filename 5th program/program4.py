class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def access_book(self):
        print("Book Title :", self.title)
        print("Author      :", self.author)
        print("Book accessed successfully!")


# Create object
book1 = Book("Python Programming", "Guido van Rossum")

# Access book
book1.access_book()