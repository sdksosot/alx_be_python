class Book:
    """Represents a book in the library"""
    
    def __init__(self, title, author):
        """
        Initialize a book with title and author
        
        Args:
            title (str): Title of the book
            author (str): Author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    def check_out(self):
        """Mark the book as checked out"""
        if self._is_checked_out:
            raise ValueError("Book is already checked out")
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned"""
        if not self._is_checked_out:
            raise ValueError("Book wasn't checked out")
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of books"""
    
    def __init__(self):
        """Initialize an empty library"""
        self._books = []  # Private list of books
    
    def add_book(self, book):
        """
        Add a book to the library
        
        Args:
            book (Book): Book object to add
        """
        if not isinstance(book, Book):
            raise TypeError("Can only add Book objects")
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by title
        
        Args:
            title (str): Title of book to check out
            
        Returns:
            bool: True if successful, False if book not found
        """
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        """
        Return a book by title
        
        Args:
            title (str): Title of book to return
            
        Returns:
            bool: True if successful, False if book not found
        """
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """Print all available books"""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books currently available")
        else:
            for book in available:
                print(book)
