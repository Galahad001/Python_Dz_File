''' 2 Реализуйте класс «Книга». Необходимо хранить в
полях класса: название книги, год выпуска, издателя,
жанр, автора, цену. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.'''

class Book():
    def __init__(self, name, year, publisher, genre, autor, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.autor = autor
        self.price = price

    def setName(self):
        self.name = input("Enter Name: ")

    def setYear(self):
        self.year = input("Enter Year: ")

    def setPublisher(self):
        self.publisher = input("Enter Publisher: ")

    def setGenre(self):
        self.genre = input("Enter Genre: ")

    def setAutor(self):
        self.autor = input("Enter Autor: ")

    def setPrice(self):
        self.price = input("Enter Price: ")

    def setAll(self):
        self.name = input("Enter Name: ")
        self.year = input("Enter Year: ")
        self.publisher = input("Enter Publisher: ")
        self.genre = input("Enter Genre: ")
        self.autor = input("Enter Autor: ")
        self.price = input("Enter Price: ")

    def getName(self):
        print(self.name)

    def getYear(self):
        print(self.year)

    def getPublisher(self):
        print(self.publisher)

    def getGenre(self):
        print(self.genre)

    def getAutor(self):
        print(self.autor)

    def getPrice(self):
        print(self.price)

    def out(self):
        print("Name - ", self.name)
        print("Year - ", self.year)
        print("Publisher - ", self.publisher)
        print("Genre - ", self.genre)
        print("Autor - ", self.autor)
        print("Price - ", self.price)


books = Book("Облачный Атлас", "2004", "ИНОСТРАНКА", "роман", "Девид Митчелл", "700 руб.")

books.out()
books.setGenre()
books.out()
# books.setAll()
# books.out()