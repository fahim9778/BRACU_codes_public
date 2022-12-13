# Create a python program to demonstrate single inheritance
class Parent:
    def func1(self):
        print("Inside Parent Class")


class Child(Parent):  # class Child is inherited from Parent class
    def func2(self):
        print("Inside Child Class")


# p = Parent()
# p.func1()

c = Child()
c.func1()
c.func2()
