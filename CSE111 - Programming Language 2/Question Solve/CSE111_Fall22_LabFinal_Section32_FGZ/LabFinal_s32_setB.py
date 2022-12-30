# Public URL (for your students): https://codecheck.io/files/22121913561u6ncxn9l02sfvhimx2y6ak14
# Edit URL (for you only): https://codecheck.io/private/problem/22121913561u6ncxn9l02sfvhimx2y6ak14/9LOMXCASVTLKRRL8CC0KIL82W

# Question Link: https://codecheck.io/private/assignment/22121913596vx1ite4l3fwau8f2jkaj1z2d/921BCBOS5UNB5I4RMYUG5K8UN
##HIDE
class Shape:
    num_sides = 0
    
    def area(self):
        return 0

class Triangle(Shape):
    num_sides = 3
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    @classmethod
    def from_sides(cls, a, b, c):
        return cls(a, b, c)
    
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

class Rectangle(Shape):
    num_sides = 4
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    @classmethod
    def from_dimensions(cls, length, width):
        return cls(length, width)
    
    @staticmethod
    def is_valid(length, width):
        return length > 0 and width > 0

class Circle(Shape):
    num_sides = 0
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
    @classmethod
    def from_radius(cls, radius):
        return cls(radius)
    
    @staticmethod
    def is_valid(radius):
        return radius > 0