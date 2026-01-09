import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "library.csv")

# ---------------- Classes ----------------
class Book:
    def __init__(self,title,author,isbn,available=True):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.available = available

    def get_isbn(self):
        return self.__isbn
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'")
            return True
        return False
        
    def return_book(self):
        self.available = True
    
    def display_info(self):
        status = "available" if self.available else "not available"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.get_isbn()}, Status: {status}")


class Ebook(Book):
    def __init__(self, title, author, isbn, size ,file_format, available=True):
        super().__init__(title, author, isbn, available)
        self.size = size
        self.file_format = file_format
    
    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}MB, Format: {self.file_format}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def search_title(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():  # case-insensitive
                return book
        return None
    
    def search_author(self,author):
        results =[]
        for book in self.books:
            if book.author.lower() == author.lower():
                results.append(book)
        return results
        
    def borrow_book(self,title):
        book = self.search_title(title)
        if book is None:
            return "Book not found"
        
        if book.borrow():
            return "BOOK BORROWED"
        else:
            return "Book not available"
    
    def return_book(self, title):
        book = self.search_title(title)
        if book is None:
            return "Book not found"

        book.return_book()
        return "Book returned successfully"


# ---------------- CSV FUNCTIONS ----------------
def save_books(library, filename=DATA_FILE):
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["type","title","author","isbn","available","size","file_format"])
            for book in library.books:
                if isinstance(book, Ebook):
                    writer.writerow([
                        "ebook",
                        book.title,
                        book.author,
                        book.get_isbn(),
                        book.available,
                        book.size,
                        book.file_format
                    ])
                else:
                    writer.writerow([
                        "book",
                        book.title,
                        book.author,
                        book.get_isbn(),
                        book.available,
                        "",
                        ""
                    ])
        print(f"Saved {len(library.books)} books to {os.path.abspath(filename)}")
    except OSError as e:
        print(f"Error saving library to {filename}: {e}")


def load_books(library, filename=DATA_FILE):
    if not os.path.exists(filename):
        return
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("type") == "ebook":
                    try:
                        size = float(row.get("size") or 0)
                    except ValueError:
                        size = 0.0
                    ebook = Ebook(
                        title=row.get("title", ""),
                        author=row.get("author", ""),
                        isbn=row.get("isbn", ""),
                        size=size,
                        file_format=row.get("file_format", ""),
                        available=row.get("available", "") == "True"
                    )
                    library.add_book(ebook)
                else:
                    book = Book(
                        title=row.get("title", ""),
                        author=row.get("author", ""),
                        isbn=row.get("isbn", ""),
                        available=row.get("available", "") == "True"
                    )
                    library.add_book(book)
        print(f"Loaded {len(library.books)} books from {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Error loading library from {filename}: {e}")


# ---------------- MAIN PROGRAM ----------------
library = Library()
load_books(library)  # Load saved books at start

while True:
    inpu=input(("--"*20)+
        "\nLIBRARY MANAGEMENT SYSTEM\nCHOOSE AN OPTION:\n"+("--"*20)+
        "\n1.Add Book\n2.Search Book\n3.Borrow Book\n4.Return Book\n5.Display All Books\n6.Exit\nEnter here:"
        
    )

    # Add Book
    if inpu=='1':
        print("--"*20)
        inp=input("Enter Book type\n1.Physical book\n2.Ebook\nEnter here:")
        if inp=='1':
            print("--"*20)
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            save_books(library)
            print("Physical book added successfully.")
            print("--"*20)


        elif inp=='2':
            print("--"*20)
            title = input("Enter ebook title: ")
            author = input("Enter ebook author: ")
            isbn = input("Enter ebook ISBN: ")
            size = float(input("Enter ebook size (in MB): "))
            file_format = input("Enter ebook file format (e.g., PDF, EPUB): ")
            ebook = Ebook(title, author, isbn, size, file_format)
            library.add_book(ebook)
            save_books(library)
            print("Ebook added successfully.")
            print("--"*20)

    # Search Book
    elif inpu=='2':
        print("--"*20)
        search=input("Search book by\n1.Title\n2.Author\nEnter here:")
        if search == '1':
            print("--"*20)
            title = input("Enter book title to search: ")
            book = library.search_title(title)
            if book:
                book.display_info()
            else:
                print("Book not found.")
        elif search == '2':
            print("--"*20)
            author = input("Enter book author to search: ")
            books = library.search_author(author)
            if books:
                for book in books:
                    book.display_info()
            else:
                print("No books found by that author.")

    # Borrow Book
    elif inpu=='3':
        print("--"*20)
        title = input("Enter book title to borrow: ")
        result = library.borrow_book(title)
        print(result)
        if result == "BOOK BORROWED":
            save_books(library)

    # Return Book
    elif inpu=='4':
        print("--"*20)
        title = input("Enter book title to return: ")
        result = library.return_book(title)
        print(result)
        if result == "Book returned successfully":
            save_books(library)

    # Display All Books
    elif inpu=='5':
        print("--"*20)
        print("All books in the library:")
        for book in library.books:
            book.display_info()

    # Exit
    elif inpu=='6':
        print("--"*20)
        save_books(library) 
        print("Exiting the library management system. Changes saved.")
        break
