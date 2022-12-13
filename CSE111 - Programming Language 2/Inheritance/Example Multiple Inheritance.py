# Create a python program to demonstrate Multiple inheritance
class Father:
    hair = ["Black", "Red", "purple"]
    Nationality = "BD"

    def func1(self):
        print("Inside Father Class")


class Mother:  # class Child is inherited from Parent class
    hair = "Red"
    Nationality = "American"

    def func2(self):
        print("Inside Mother Class")


class Child(Mother, Father):
    Nationality = Mother.Nationality

    def func3(self):
        print("Inside Child Class")

    def showMyBehavior(self):
        type(self).hair = ["Blue"]
        print(type(self).hair, type(self).Nationality)


g = Child()
g.func3()
g.func2()
g.func1()
g.showMyBehavior()

print(Father.hair)

help(g)
g2 = Child()
g2.showMyBehavior()
print(Father.hair)


