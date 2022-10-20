#Creating library class
from typing import ClassVar


class Library:
    
    def __init__(self, listOfBooks): #Creating an instance and taking info about list of books from the user
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for books in self.books:
            print(" *", books)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have borrowed {bookName} book. \n Please keep it safe and return it on time.")
            self.books.remove(bookName)
            return True

        else:
            print("This book is either not available or has already been issued to someone else. Please wait until the book is available.")
            return False

    def returnbook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the book. Hope you enjoyed reading it!")

#Creating student class
class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow?? ")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return/add?? ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["C++", "Python", "Python for Professional", "Java"])
    student = Student()
    # centralLibrary.displayAvailableBooks()

    while(True):
        welcomeMsg = """=====Welcome to Central Library=====
        Please choose an option:
        1. List of Books
        2. Request a book
        3. Add/Return a Book
        4. Exit the Library
        """
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()  

        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())

        elif a == 3:
            centralLibrary.returnbook(student.returnBook())

        elif a == 4:
            print("Thanks for choosing Central Library. Have a Great Day Ahead!")
            exit()

        else:
            print("Invalid Choice!")

        