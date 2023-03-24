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