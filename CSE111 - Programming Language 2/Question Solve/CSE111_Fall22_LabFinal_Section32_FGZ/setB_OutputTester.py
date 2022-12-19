from LabFinal_s32_setB import *

triangle = Triangle.from_sides(3, 4, 5)
print(triangle.area()) # 6
print("Expected: 6")
print(Triangle.is_valid(3, 4, 5)) # True
print("Expected: True")
print(Triangle.is_valid(1, 2, 3)) # False
print("Expected: False")

rectangle = Rectangle.from_dimensions(3, 4)
print(rectangle.area()) # 12
print("Expected: 12")
print(Rectangle.is_valid(3, 4)) # True
print("Expected: True")
print(Rectangle.is_valid(1, 2)) # True
print("Expected: True")

circle = Circle.from_radius(2)
print(circle.area()) # 12.56
print("Expected: 12.56")
print(Circle.is_valid(2)) # True
print("Expected: True")
print(Circle.is_valid(1)) # True
print("Expected: True")