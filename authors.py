class book:
    total_books = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author

        book.total_books += 1

    def get_info(self):
        return f"{self.title} by {self.author}"

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and len(title) > 0
    
book1 = book("The Catcher in the Rye", "J.D. Salinger")
book2 = book("To Kill a Mockingbird", "Harper Lee")


print(book1.get_info())
print(book2.get_info())

print(book.get_total_books())

print(book.is_valid_title("The Catcher in the Rye"))