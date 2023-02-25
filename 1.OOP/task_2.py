# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте так,
# что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
class Book:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.obj = BookReview()

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"Author: {self.author}\nName: {self.name},{self.year}\ngenre: {self.genre}\n{self.obj.show_review()}"

    def __str__(self):
        return f"{self.author} {self.name} {self.year} {self.genre}"


class BookReview:
    @staticmethod
    def get_review():
        review = input('Enter a review of this book: ')
        return f'Review: {review}'

    def show_review(self):
        return self.get_review()


book_1 = Book('R.Kipling', 'Jungle Book', 1893, 'novel')
book_2 = Book('H.Melville', 'Moby Dick', 1851, 'adventure')
book_3 = Book('M.Mitchell', 'Gone with the Wind', 1936, 'love story')
for book in [book_1, book_2, book_3]:
    print(f"What's your opinion about '{book.name}'?")
    print(f'{book.__repr__()}\n')
