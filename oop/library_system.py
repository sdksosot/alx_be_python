class Book:
    """Base class representing a generic book."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title: str, author: str, file_size: int) -> None:
        super().__init__(title, author)
        self.file_size = int(file_size)

    def __str__(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title: str, author: str, page_count: int) -> None:
        super().__init__(title, author)
        self.page_count = int(page_count)

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Composition class that manages a collection of books."""

    def __init__(self) -> None:
        self.books = []  # list[Book]

    def add_book(self, book) -> None:
        """Add a Book (or subclass) instance to the library."""
        if not isinstance(book, Book):
            raise TypeError("add_book expects an instance of Book or one of its subclasses")
        self.books.append(book)

    def list_books(self) -> None:
        """Print details for every book in the library."""
        for book in self.books:
            print(str(book))
