class Book():
    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        self.year = year
        title = "война и мир"
        author = "Л. Н. Толстой"
        year = "1869"
    def info(self):
        print("Книга:", self.title)
        print("Автор:", self.author)
        print("Год:", self.year)
        return

if __name__ == '__main__':
    book = Book(title = "война и мир", author = "Л. Н. Толстой", year = "1869")
    book.info()