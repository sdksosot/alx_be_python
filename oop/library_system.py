class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.b = "Book"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
        self.b = "EBook"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
        self.b = "PrintBook"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"{book.b}: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"{book.b}: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"{book.b}: {book.title} by {book.author}")


