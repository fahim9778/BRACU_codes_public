# Create a python program to demonstrate Multilevel inheritance
class Parent:
    def func1(self):
        print("Inside Parent Class")


class Child(Parent):  # class Child is inherited from Parent class
    def func2(self):
        print("Inside Child Class")


class Grandchild(Child):
    def func3(self):
        print("Inside Grandchild Class")

c = Child()
g = Grandchild()
g.func3()
g.func2()
g.func1()
print(help(c))
