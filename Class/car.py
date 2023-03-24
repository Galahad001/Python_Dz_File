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