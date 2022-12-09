class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name
    
    def getName(self):
        return self.name
    
    def hasFormalin(self):
        return self.__formalin

class Mango(Fruit):
    def __init__(self):
        super().__init__(True, "Mango")

    def __repr__(self):
        if self.hasFormalin():
            return f"{self.getName()}s are bad for you."
        else:
            return f"{self.getName()}s are good for you."
    
class Jackfruit(Fruit):
    def __init__(self):
        super().__init__(False, "Jackfruit")

    def __repr__(self):
        if self.hasFormalin():
            return f"{self.getName()}s are bad for you."
        else:
            return f"{self.getName()}s are good for you."
    
class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print('Do not eat the',f.getName(),'.')
            print(f)
        else:
            print('Eat the',f.getName(),'.')
            print(f)
        
m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)

