class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.__is_available = True

    # Checking the availability of the book
    def is_available(self):
        return self.__is_available

    # Borrow the book
    def borrow_book(self):
        if not self.__is_available:
            raise Exception("This book is currently borrowed.")
        self.__is_available = False

    # Return the book
    def return_book(self):
        if self.__is_available:
            raise Exception("This book is already available.")
        self.__is_available = True

    # Display information
    def display_info(self):
        status = "Available" if self.__is_available else "Not Available"
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.year}")
        print(f"Status: {status}")

