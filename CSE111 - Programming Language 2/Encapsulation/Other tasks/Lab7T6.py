class Shape:

  def __init__(self, name='Default', height=0, base=0):
    self.area = 0
    self.name = name
    self.height = height
    self.base = base

  def get_height_base(self):
    return "Height: "+str(self.height)+",Base: "+str(self.base)


class triangle(Shape):
    def __init__(self, name='Default', height=0, base=0):
        Shape.__init__(self, name, height, base)
    
    def calcArea(self):
        self.area = (self.height * self.base)/2
        return self.area

    def printDetail(self):
        return "Shape name: " + str(self.name) +"\n" + super().get_height_base() + "\nArea: "+str(self.calcArea())

class trapezoid(Shape):
    def __init__(self, name='Default', height=0, base=0, side_a=0):
        Shape.__init__(self, name, height, base)
        self.side_a = side_a
    
    def calcArea(self):
        return (self.base + self.side_a) * self.height / 2

    def printDetail(self):
        return "Shape name: " + str(self.name) +"\n" + super().get_height_base() + ", Side_A: "+str(self.side_a) + "\nArea: "+str(self.calcArea())
#write your code here

tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())
