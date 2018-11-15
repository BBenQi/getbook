from db.data import get_books


class BookService:
    def __init__(self):
        self.book = get_books()

    def say_book(self):
        print(self.book)
