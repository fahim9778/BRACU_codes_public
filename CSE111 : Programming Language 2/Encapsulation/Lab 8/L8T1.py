class RealNumber:
    
    def __init__(self, r=0):
        self.__realValue = r  
    def getRealValue(self):
        return self.__realValue
    def setRealValue(self, r):
        self.__realValue = r
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())

class ComplexNumber(RealNumber):
    
    def __init__(self, r=1.0, i=1.0):
        RealNumber.__init__(self, float(r))
        self.__imaginaryValue = float(i)
    def getImaginaryValue(self):
        return self.__imaginaryValue
    def setImaginaryValue(self, i):
        if isinstance(i, int):
            self.__imaginaryValue = float(i)
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())+'\nImaginaryPart: '+str(self.getImaginaryValue())

cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)
