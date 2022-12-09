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

    @staticmethod
    def canIBuyIt(myAbility):
        if myAbility > 10000:
            print("Yes you can buy it!")
        else:
            print("Sorry Poor guy!")

    def __str__(self):
        return f"{type(self).year}"


Car.canIBuyIt(5_000)
Car.canIBuyIt(1_00_000.6_888_88)

toyotaCamry = Car("Toyota", "Camry", 2015)
toyotaCamry.canIBuyIt(10000000000000)