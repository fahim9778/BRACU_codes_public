# Create a class for complex numbers 
# and overload the + operator to add two complex numbers

class Complex:
    ##CALL 5, 6
    def __init__(self, real, img):
        self.real = real
        self.img = img

    ##CALL 5, 6
    def __add__(self, other):
        ##HIDE
        return Complex(self.real + other.real, self.img + other.img)
        ##EDIT return . . .

    def __str__(self):
        ## The result should be in the form of a + bi
        ##HIDE
        return str(self.real) + " + " + str(self.img) + "i"
        ##EDIT return . . .


