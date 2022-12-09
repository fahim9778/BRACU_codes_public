# Create an example of instance method
class Car:
    says = "Vroom Vroom"
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def details(self): # INSTANCE METHOD
        print("Car details")
        print(f"Manufacturer : {self.make}")
        print(f"Model of the Car: {self.model}")
        print(f"Built in year: {self.year}")

toyotaCamry = Car("Toyota", "Camry", 2015)

toyotaCamry.details()
print(toyotaCamry.year)
toyotaCamry.year = 2016
toyotaCamry.details()

print(toyotaCamry.says)
toyotaCamry.says = "Broom Broomm Brooooommmmm"
print(Car.says)

