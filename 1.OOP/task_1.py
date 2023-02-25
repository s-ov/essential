# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре.
# Создайте несколько разных книг. Определите для него операции проверки на равенство и неравенство,
# методы __repr__ и __str__.
class Book:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"Author: {self.author}; Name: {self.name},{self.year}; genre: {self.genre} "

    def __str__(self):
        return f"{self.author} {self.name} {self.year} {self.genre}"


book_1 = Book('R.Kipling', 'Jungle Book', 1893, 'novel')
book_2 = Book('H.Melville', 'Moby Dick', 1851, 'adventure')
book_3 = Book('M.Mitchell', 'Gone with the Wind', 1936, 'love story')
book_4 = Book('R.Kipling', 'Jungle Book', 1893, 'novel')
books = [book_1, book_2, book_3, book_4]
for book in books:
    print(book.__repr__())
print(book_1 == book_3)
print(book_1 == book_4)
