class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print("Inside Father class")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


f1 = Father("John", 45)
f1.print_details()


class Son(Father):
    def __init__(self, s_name, s_age, tech):
        super().__init__(s_name, s_age)
        self.tech = tech

    def print_details(self):
        print("Inside Son class")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Tech: {self.tech}")


s1 = Son("Jasson", 30, "Python")
s1.print_details()


class Grandson(Son):
    def __init__(self, name, age, tech, pet):
        Father.__init__(self, name, age)
        self.tech = tech
        self.pet = pet

    def print_details(self):
        print("Inside Grandson class")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        # print(f"Tech: {self.tech}")
        print(f"Pet : {self.pet}")


g1 = Grandson("Jonnas", 6, "Java", "Nanobot")
g1.print_details()