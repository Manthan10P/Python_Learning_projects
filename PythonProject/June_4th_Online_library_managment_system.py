class book:
    def __init__(self,book_id, title, author):
        self.book_id = book_id #encapsulated private
        self.title = title
        self.author = author

    def dispaly(self):
        print(f"Book Id : {self.book_id}")
        print(f'Title : {self.title}')
        print(f'author : {self.author}')

#object creation
book1 = book("B101","Python","john Doe")
book1.dispaly()

#inheritance [Ebook inherits Book]
class Ebook(book):
    def __init__(self,book_id,title,author,file_size):
        super().__init__(book_id,title,author)
        self.file_size = file_size

    def dispaly(self):
        super().dispaly()
        print(f"File Size : {self.file_size} MB ")

print("----------------------------------------------------------------------------")

#objects creation
ebook1 = Ebook("E202","Python for pros", "john smith" , 10)
ebook1.dispaly()

print("----------------------------------------------------------------------------")

#abstraction (library with internal logic hidden)
class library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        #abstracting internal logic
        self.books.append(book)
        print (f"{book.title} added to library./n")

    def show_all_books(self):
        print("/n.--------------------------Library books--------------------------")
        for book in self.books:
            book.dispaly()
            print("------------")

#bringing everything together
library = library()

book1 = book("B101","Python","john Doe")
ebook1 = Ebook("E202","Python for pros", "john smith" , 10)

library.add_book(book1)
library.add_book(ebook1)

library.show_all_books()