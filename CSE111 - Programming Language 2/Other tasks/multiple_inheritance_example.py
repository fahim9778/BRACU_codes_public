class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = "Male"
        self.har_color = "Black"

class Mother:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = "Female"
        self.har_color = "Red"
       
class Child(Mother, Father):
    def __init__(self, name, age, technology):
        super().__init__(name, age)
        self.technology = technology
    
    def print_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Hair Color: ", self.har_color)
        print("Technology: ", self.technology)
        print("==============================")

c1 = Child("John", 20, "Python")
c1.print_details()

c2 = Child("Jane", 20, "Java")
c2.print_details()
