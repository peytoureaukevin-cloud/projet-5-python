class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books_list = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return

        print(f"Le livre '{book_title}' n'est pas disponible dans la bibliothèque.")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books_list.append(book)
                return

        print(f"Le livre '{book_title}' n'est pas disponible pour l'emprunt.")

    def return_book(self, book_title):
        for book in self.borrowed_books_list:
            if book.title == book_title:
                self.borrowed_books_list.remove(book)
                self.books.append(book)
                return

        print(f"Le livre '{book_title}' n'a pas été emprunté.")

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books(self):
        return [book.title for book in self.borrowed_books_list]