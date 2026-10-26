"""
LIBRARY MANAGEMENT SYSTEM
Features: Add Book, Register Patron, View Books and Patrons,
Borrow Book, and Return Book.
"""

class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True
        self.borrowed_by = None

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrowed_by}"
        return f"[{self.isbn}] '{self.title}' by {self.author} - {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name

    def __str__(self):
        return f"[{self.patron_id}] {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, isbn, title, author):
        if isbn in self.books:
            print("A book with this ISBN already exists.")
            return
        self.books[isbn] = Book(isbn, title, author)
        print(f"Book added: {self.books[isbn]}")

    def register_patron(self, patron_id, name):
        if patron_id in self.patrons:
            print("A patron with this ID is already registered.")
            return
        self.patrons[patron_id] = Patron(patron_id, name)
        print(f"Patron registered: {self.patrons[patron_id]}")

    def view_books_and_patrons(self):
        print("\n--- Books ---")
        if not self.books:
            print("No books in library.")
        for book in self.books.values():
            print(book)

        print("\n--- Patrons ---")
        if not self.patrons:
            print("No patrons registered.")
        for patron in self.patrons.values():
            print(patron)

    def borrow_book(self, isbn, patron_id):
        book = self.books.get(isbn)
        if book is None:
            print("Not Available: no such book.")
        elif patron_id not in self.patrons:
            print("Not Available: unknown patron.")
        elif book.available:
            book.available = False
            book.borrowed_by = patron_id
            print(f"Issued '{book.title}' to patron {patron_id}.")
        else:
            print("Not Available.")

    def return_book(self, isbn, patron_id):
        book = self.books.get(isbn)
        if book is not None and not book.available and book.borrowed_by == patron_id:
            book.available = True
            book.borrowed_by = None
            print(f"Return accepted for '{book.title}'.")
        else:
            print("Book not borrowed by this patron.")


def user_selects_operation():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. View Books & Patrons")
    print("4. Borrow Book")
    print("5. Return Book")
    return input("Choose an option (1-5): ").strip()


def main():
    library = Library()
    while True:
        choice = user_selects_operation()

        if choice == "1":
            isbn = input("Enter ISBN: ").strip()
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            library.add_book(isbn, title, author)
        elif choice == "2":
            patron_id = input("Enter patron ID: ").strip()
            name = input("Enter patron name: ").strip()
            library.register_patron(patron_id, name)
        elif choice == "3":
            library.view_books_and_patrons()
        elif choice == "4":
            isbn = input("Enter ISBN to borrow: ").strip()
            patron_id = input("Enter patron ID: ").strip()
            library.borrow_book(isbn, patron_id)
        elif choice == "5":
            isbn = input("Enter ISBN to return: ").strip()
            patron_id = input("Enter patron ID: ").strip()
            library.return_book(isbn, patron_id)
        else:
            print("Invalid option. Please choose 1-5.")

        cont = input("\nContinue? (Yes/No): ").strip().lower()
        if cont in ("no", "n"):
            break
    print("\nEND")


if __name__ == "__main__":
    main()
