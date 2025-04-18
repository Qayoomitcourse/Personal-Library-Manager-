import json


class BookCollection:
    """ A class to manage a collection of books, allowing users to store, add, remove, and search for books """

    def __init__(self):
        """ Initialization a new collection with an empty list and set up the file storage """
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()
    
    def read_from_file(self):
        """Load saved books from the json file into memory.
        if the file does not exist or in corrupted, start with an empty collection"""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except FileNotFoundError:
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a json file for permanent storage"""
        try:
            with open(self.storage_file, "w") as file:
                json.dump(self.book_list, file, indent=4)
        except Exception as e:
            print(f"Error saving to file: {e}")
    
    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user"""
        book_title = input("Enter book title: ")
        book_author = input("Enter author : ")
        publication_year = input("Enter publication year : ")
        book_genre = input("Enter genre : ")
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )
        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }
        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added successfully!\n")
    
    def remove_book(self):
        """Remove a book from the collection by its title"""
        book_title = input("Enter the title of the book to remove: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")

    def search_book(self):
        """Search for a book by its title or author"""
        search_type = input("Search by:\n1 - Title\n2 - Author\n Enter your choice: ")
        search_text = input("Enter the search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]
        if found_books:
           print("Matching books:")
           for index, book in enumerate(found_books, start=1):
            read_status = "Read" if book["read"] else "Not Read"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) ({book['genre']}) - {read_status}")
        else:
          print("No books found matching the search criteria.")
    
    def update_book(self):
        """Update the details of a book by its title"""
        book_title = input("Enter the title of the book to update: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Current book details:")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Year: {book['year']}")
                print(f"Genre: {book['genre']}")
                print(f"Read: {'Yes' if book['read'] else 'No'}")
                
                update_choice = input("What would you like to update?\n1 - Title\n2 - Author\n3 - Year\n4 - Genre\n5 - Read Status\nEnter your choice: ")
                
                if update_choice == "1":
                    new_title = input("Enter the new title: ")
                    book["title"] = new_title   
                elif update_choice == "2":
                    new_author = input("Enter the new author: ")
                    book["author"] = new_author
                elif update_choice == "3":
                    new_year = input("Enter the new year: ")
                    book["year"] = new_year 
                elif update_choice == "4":
                    new_genre = input("Enter the new genre: ")
                    book["genre"] = new_genre
                elif update_choice == "5":
                    new_read_status = input("Enter the new read status (yes/no): ").strip().lower() == "yes"
                    book["read"] = new_read_status  
                    
                self.save_to_file()
                print("Book updated successfully!\n")
                return
        print("Book not found in the collection.") 
                
    def display_books(self):
        """Display all books in the collection"""
        if not self.book_list:
            print("No books available in the collection.")
        else:
            print("All books in the collection:")
            for index, book in enumerate(self.book_list, start=1):
                read_status = "Read" if book["read"] else "Not Read"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) ({book['genre']}) - {read_status}")
    
    def view_reading_progress(self):
        """Display the reading progress of the collection"""
        if not self.book_list:
            print("No books available in the collection.")
        else:
            total_books = len(self.book_list)
            read_books = sum(1 for book in self.book_list if book["read"])
            percentage_read = (read_books / total_books) * 100
            print(f"Total books: {total_books}")
            print(f"Books read: {read_books}")
            print(f"Percentage of books read: {percentage_read:.2f}%")          
           
    
    def start_application(self):
        while True:
            print("📚 Welcome to the Book Collection Application!📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for book")
            print("4. update book details")
            print("5. Display all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.remove_book()
            elif user_choice == "3":
                self.search_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.display_books()
            elif user_choice == "6":
                self.view_reading_progress()
            elif user_choice == "7":
                print("Exiting the application...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
                
                

            
            
            
