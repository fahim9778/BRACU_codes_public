"Write the Mango and the Jackfruit classes so that the following code generates the output below:"

class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name
    
    def getName(self):
        return self.name
    
    def hasFormalin(self):
        return self.__formalin
    
class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print('Do not eat the',f.getName(),'.')
            print(f)
        else:
            print('Eat the',f.getName(),'.')
            print(f)

class Mango(Fruit):
    def __init__(self, formalin=True, name='Mango'):
        super().__init__(formalin, name)
    def __str__(self):
        if self.hasFormalin():
            return self.name + 's are bad for you.'
        else:
            return self.name + 's are good for you.'

class Jackfruit(Fruit):
    def __init__(self, formalin=False, name='Jackfruit'):
        super().__init__(formalin, name)
    def __str__(self):
        if self.hasFormalin():
            return self.name + 's are bad for you.'
        else:
            return self.name + 's are good for you.'

m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)