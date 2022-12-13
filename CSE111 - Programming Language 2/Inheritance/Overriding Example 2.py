class GrandParent:
    _title = "Khan"  # Protected Variable
    __wealth = "1 Crore"  # Private Variable

    def func1(self):
        print("Inside GrandParent Class")

    def func4(self):
        print("Inside GrandParent Class 2")


class Parent(GrandParent):
    _title = "Ullah"  # Variable Overriding

    def func2(self):
        print("Inside Parent Class")


class Child(Parent):
    def func1(self):
        print("Party !!!")  # Method Overriding

    def func3(self):
        print("Inside Child Class")

c2 = Child()
c2.func1()
c2.func2()
c2.func3()

print(c2._title)

# print(c2.__wealth) # Error. Because Private Variable doesn't pass through the descendants

help(c2)