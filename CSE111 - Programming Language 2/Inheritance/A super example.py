class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = "Male"
        self.hair_color = "Black"


class Child(Parent):
    def __init__(self, c_name, c_age, school):
        super().__init__(c_name, c_age)
        self.school = school

    def print_details(self):
        print(f"Name : {self.name}")
        print(f"Age: {self.age}")
        print(f"school : {self.school}")

    @classmethod
    def print_class_details(cls):
        print(f"Class Name : {cls.__name__}")
        print(f"Class Doc : {cls.__doc__}")
        print(f"Class Module : {cls.__module__}")
        print(f"Class Base : {cls.__bases__}")


class Grandchild(Child):
    def __init__(self, g_name, g_age, g_school, g_pet):
        super().__init__(g_name, g_age, g_school)
        self.pet = g_pet

    def print_details(self):  # Method overriding
        super().print_details()
        print(f"Pet : {self.pet}")


p1 = Parent("Don", 60)
print(p1.name, p1.age)

c1 = Child("John", 30, "BRACU")
c1.print_details()

gc1 = Grandchild("Susan", 26, "NSU", "Nanobot")
gc1.print_details()

print(issubclass(Grandchild, Parent))
