''' 1 Реализуйте класс «Автомобиль». Необходимо хранить
в полях класса: название модели, год выпуска, произво-
дителя, объем двигателя, цвет машины, цену. Реализуйте
методы класса для ввода данных, вывода данных, реа-
лизуйте доступ к отдельным полям через методы класса.'''

class Car():
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price
        
    def setModel(self):
        self.model = input("Enter Model: ")

    def setYear(self):
        self.year = input("Enter Year: ")

    def setManufacturer(self):
        self.manufacturer = input("Enter Manufacturer: ")

    def setEngine_Capacity(self):
        self.engine_capacity = input("Enter Engine_Capacity: ")

    def setColor(self):
        self.color = input("Enter Color: ")

    def setPrice(self):
        self.price = input("Enter Price: ")

    def setAll(self):
        self.model = input("Enter Model: ")
        self.year = input("Enter Year: ")
        self.manufacturer = input("Enter Manufacturer: ")
        self.engine_capacity = input("Enter Engine_Capacity: ")
        self.color = input("Enter Color: ")
        self.price = input("Enter Price: ")

    def getModel(self):
        print(self.model)

    def getYear(self):
        print(self.year)

    def getManufacturer(self):
        print(self.manufacturer)

    def getEngine_Capacity(self):
        print(self.engine_capacity)

    def getColor(self):
        print(self.color)

    def getPrice(self):
        print(self.price)

    def out(self):
        print("Model - ", self.model)
        print("Year - ", self.year)
        print("Manufacturer - ", self.manufacturer)
        print("Engine-capacity - ", self.engine_capacity)
        print("Color - ", self.color)
        print("Price - ", self.price)

car_0 = Car("G AMG", "2022", "Mercedes-Benz", "585 л.с.", "Black", "30.000.000")

car_0.out()
car_0.setColor()
car_0.out()


print("=" * 15, "1", "=" * 15)


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


print("=" * 15, "1", "=" * 15)


''' 3 Реализуйте класс «Стадион». Необходимо хранить в
полях класса: название стадиона, дату открытия, страну,
город, вместимость. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.'''

class Stadium():
    def __init__(self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity

    def setName(self):
        self.name = input("Enter Name: ")

    def setYear(self):
        self.year = input("Enter Year: ")

    def setCountry(self):
        self.country = input("Enter Country: ")

    def setCity(self):
        self.city = input("Enter City: ")

    def setCapacity(self):
        self.capacity = input("Enter Capacity: ")

    def setAll(self):
        self.name = input("Enter Name: ")
        self.year = input("Enter Year: ")
        self.country = input("Enter Country: ")
        self.city = input("Enter City: ")
        self.capacity = input("Enter Capacity: ")

    def getName(self):
        print(self.name)

    def getYear(self):
        print(self.year)

    def getPublisher(self):
        print(self.country)

    def getGenre(self):
        print(self.city)

    def getAutor(self):
        print(self.capacity)

    def out(self):
        print("Name - ", self.name)
        print("Year - ", self.year)
        print("Country - ", self.country)
        print("City - ", self.city)
        print("Capacity - ", self.capacity)

stadium_0 = Stadium("Стадион", "2000", "Бразилия", "Рио-де-Жанейро", "не знаю")

stadium_0.out()
stadium_0.setCapacity()
stadium_0.out()