from library_manager import LibraryManager

def main():
    library = LibraryManager()
    
    while True:
        print("\nLibrary Manager System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book") 
        print("4. Display All Books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        #Add Book
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            library.add_book(title, author, year)
            
        #Borrow Book
        elif choice == '2':
            library.display_all_books()
            title = input("\nEnter book title to borrow: ")
            library.borrow_book(title)
            
        #Return Book
        elif choice == "3":
            title = input("Enter book title to return: ")
            library.return_book(title)
            
        #Display All Books
        elif choice == '4':
            library.display_all_books()
            
        elif choice == '5':
            print("Exiting the Library Manager System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
            
            
#Run the main function
if __name__ == "__main__":
    main()