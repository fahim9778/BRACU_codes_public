class Car:
    says = "Vroom Vroom"
    make = None
    model = None
    year = None

    def __init__(self, make, model, year):
        type(self).make = make
        Car.model = model
        type(self).year = year

    def details(self): # INSTANCE METHOD
        print("Car details")
        print(f"Manufacturer : {self.make}")
        print(f"Model of the Car: {self.model}")
        print(f"Built in year: {self.year}")

    @classmethod
    def pricerange(cls): # CLASS METHOD
        if cls.make == "Toyota":
            print("Expensive Car")
        elif cls.make == "Audi":
            print("A way more Expensive e Car")
        else:
            print("No data available!")

    @classmethod
    def changeSays(cls, newSays):
        cls.says = newSays

    @classmethod
    def from_string(cls, car_info):
        car_manuf, car_model, car_year = car_info.split("-")
        return cls(car_manuf, car_model, car_year)

Car.make = "Toyota"
Car.pricerange()
Car.make = "Audi"
Car.pricerange()

toyotaCamry = Car("Toyota", "Camry", 2015)
toyotaCamry.pricerange()

Car.changeSays("Brommmmmmmm")
print(Car.says)

toyotaCamry.changeSays("Troooommmmmm")
print(toyotaCamry.says)

print(Car.says)

audiCar = Car.from_string("Audi-A1-2017") # ALTERNATIVE CONSTRUCTOR or Factory Method Constructor
audiCar.details()