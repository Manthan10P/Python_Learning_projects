# Base class
class Library:
    def __init__(self, books):
        self.books = books  # List of book titles
        self.borrowed_books = {}

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f" - {book}")

    def borrow_book(self, book_name, user_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.borrowed_books[book_name] = user_name
            print(f"{user_name} borrowed '{book_name}'")
        else:
            print(f"'{book_name}' is not available.")

    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.books.append(book_name)
            user = self.borrowed_books.pop(book_name)
            print(f"{user} returned '{book_name}'")
        else:
            print(f"'{book_name}' was not borrowed.")

# Derived class
class User:
    def __init__(self, name):
        self.name = name

    def request_book(self):
        return input("Enter the book name you want to borrow: ")

    def return_book(self):
        return input("Enter the book name you want to return: ")

# Main function
def main():
    lib = Library(["Python Basics", "OOP Concepts", "Data Structures"])
    user = User("Manthan")

    while True:
        print("\n----- Menu -----")
        print("1. Display Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            lib.display_books()
        elif choice == "2":
            book = user.request_book()
            lib.borrow_book(book, user.name)
        elif choice == "3":
            book = user.return_book()
            lib.return_book(book)
        elif choice == "4":
            print("Thank you for using the Library System!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
