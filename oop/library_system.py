class Book:
    def __init__(self,title:str,author:str):
        self.title = title
        self. author = author
        self.b = 'Book:'
class EBook(Book):
    def __init__(self, file_size:int):
        self.file_size = file_size
        self.b = 'EBook:'
        super().__init__()
class PrintBook(Book):
    def __init__(self, page_count:int):
        self.page_count = page_count
        self.b = 'PrintBook:'
        super().__init__()
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        for book in self.books:
            if self.books:
                print(f"{book.b}: {book.title} by {book.author}")

        

        