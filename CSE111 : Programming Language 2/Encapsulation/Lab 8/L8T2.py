class RealNumber:
    def __init__(self, number=0):
        self.number = number
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)

class ComplexNumber(RealNumber):
    def __init__(self, real=0, imaginary=0):
        if not isinstance(real, RealNumber):
            real = RealNumber(real)
        RealNumber.__init__(self, real)
        self.imaginary = imaginary
    def __add__(self, anotherComplexNumber):
        # if isinstance(self.number, int):
        #     self.number = RealNumber(self.number)
        # if isinstance(anotherComplexNumber.number, int):
        #     anotherComplexNumber.number = RealNumber(anotherComplexNumber.number)
        return ComplexNumber(self.number + anotherComplexNumber.number, self.imaginary + anotherComplexNumber.imaginary)
    def __sub__(self, anotherComplexNumber):
        # if isinstance(self.number, int):
        #     self.number = RealNumber(self.number)
        # if isinstance(anotherComplexNumber.number, int):
        #     anotherComplexNumber.number = RealNumber(anotherComplexNumber.number)
        return ComplexNumber(self.number - anotherComplexNumber.number, self.imaginary - anotherComplexNumber.imaginary)
    def __str__(self):
        if self.imaginary < 0:
            return f"{self.number} - {-self.imaginary}i"
        else:
            return str(self.number) + ' + ' + str(self.imaginary) + 'i'

r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)
