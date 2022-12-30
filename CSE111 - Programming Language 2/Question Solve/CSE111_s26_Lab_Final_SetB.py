class Validator:
    shapeCount = 0

    def __init__(self, name):
        self.name = name
        self.valid = False
        Validator.shapeCount += 1

    def rectangle_validator_angles(self, angles):
        if sum(angles) == 360:
            self.valid = True

    def rectangle_validator_sides(self, sides):
        sorted_sides = sorted(sides)
        if sum(sorted_sides[0:3]) > sorted_sides[3]:
            self.valid = True

    def getName(self):
        return self.name

    @classmethod
    def printShapeCount(cls):
        print(f"Total Shape: {cls.shapeCount}")

    def __str__(self):
        if self.valid:
            return f"This is an valid shape."
        else:
            return f"This is a invalid shape."


class Shape(Validator):
    def __init__(self, name, angles=[], sides=[]):
        super().__init__(name)
        self.angles = angles
        self.sides = sides

    def validate(self):
        if len(self.angles) != 0:
            super().rectangle_validator_angles(self.angles)
        elif len(self.sides) != 0:
            super().rectangle_validator_sides(self.sides)

    def __str__(self):
        print(super().__str__())
        return f"Shape Name: {super().getName()}."


# Driver Code
t1 = Shape("Rectangle 1", angles=[90, 60, 30, 180])
print(t1.valid)
print(t1)
t1.validate()
print(t1)
print("=======================")
t2 = Shape("Rectangle 2", sides=[5, 4, 3, 6])
print(t2.valid)
print(t2)
t2.validate()
print(t2)
print("=======================")
Validator.printShapeCount()
print("=======================")
t3 = Shape("Rectangle 3", angles=[90, 60, 45, 120])
print(t3)
t3.validate()
print(t3)
print("=======================")
t4 = Shape("Rectangle 4", sides=[5, 4, 9, 2])
print(t4)
t4.validate()
print(t4)
print("=======================")
Validator.printShapeCount()
print("=======================")
