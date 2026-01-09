# Library-management

📚 Library Management System (Python OOP + CSV)

A console-based Library Management System built using Python Object-Oriented Programming (OOP) principles.
This project allows users to manage physical books and eBooks, borrow and return books, search the library, and persist data using CSV files.

🚀 Features

📘 Add Physical Books

📱 Add EBooks (with file size and format)

🔍 Search books by Title or Author

📖 Borrow and return books

📋 Display all books in the library

💾 Persistent storage using CSV (data is saved on exit)

🧠 Implements core OOP concepts

🧱 OOP Concepts Used
Concept	Implementation
Class & Object	Book, Ebook, Library
Encapsulation	ISBN is private (__isbn)
Inheritance	Ebook inherits from Book
Polymorphism	display_info() overridden in Ebook
Abstraction	Library handles book operations internally
🗂 Project Structure
library-management-system/
│
├── library.py        # Main Python program
├── library.csv       # Auto-generated data file
└── README.md         # Project documentation

🛠 Technologies Used

Python 3

Built-in csv module

Built-in os module

▶️ How to Run the Project

Clone the repository

Navigate to the project folder

cd library-management-system

Run the program

python library.py

📌 Menu Options
LIBRARY MANAGEMENT SYSTEM
1. Add Book
2. Search Book
3. Borrow Book
4. Return Book
5. Display All Books
6. Exit

💾 Data Persistence (CSV)

All books are saved in library.csv

Data is loaded automatically when the program starts

Changes are saved only when exiting the system

CSV Format:
type,title,author,isbn,available,size,file_format

🧪 Example Usage

Add books (physical or ebook)

Search by title or author

Borrow a book (availability updates)

Return a book

Exit and restart — data remains saved ✔️

🎯 Learning Outcomes

By building this project, you will understand:

How to design real-world systems using OOP

How to use inheritance and encapsulation properly

How to persist data without a database

How to structure a menu-driven console application

📈 Future Improvements

User authentication system

Due dates and fines

Export reports

GUI using Tkinter / PyQt

Database integration (SQLite)

👨‍💻 Author

Kamal Nayan Thakur
Python & AI/ML Enthusiast 🚀

⭐ Support

If you found this project helpful:

⭐ Star the repository

🍴 Fork it

🧠 Improve it
