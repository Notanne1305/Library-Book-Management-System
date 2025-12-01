from book import Book

class LibraryManager:
    def __init__(self):
        print("LibraryManager.__init__ called")
        self.books = []
        
    #Add a new book
    def add_book(self, title, author, year):
        try:
            if not title or not author or not year:
                raise ValueError("All fields are required.")
            
            new_book = Book(title, author, year)
            self.books.append(new_book)
            print(f"\n'{title}' added successfully!")
        except Exception as e:
            print(f"Error adding book: {e}")
            
    #Search book by title
    def find_book_by_title(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    #Borrow a book
    def borrow_book(self, title):
        try:
            book = self.find_book_by_title(title)
            if book is None:
                raise ValueError("Book not found")
            
            book.borrow_book()
            print(f"\nYou have successfully borrowed '{book.title}'")
        except Exception as e:
            print(f"Error: {e}")
            
    #Return a book
    def return_book(self, title):
        try:
            book = self.find_book_by_title(title)
            if book is None:
                raise ValueError("Book not found")
            
            book.return_book()
            print(f"\nYou have successfully returned '{book.title}'")
        except Exception as e:
            print(f"Error: {e}")
            
            
    #Display all books
    def display_all_books(self):
        books = getattr(self, 'books', None)
        if not books:
            print("\nNo books in the library.")
            return
        
        print("\nBooks in the Library:")
        for book in books:
            book.display_info()
