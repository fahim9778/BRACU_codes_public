from multipledispatch import dispatch

class MultiCalculator:
    def __init__(self):
        pass

    # @dispatch(int, int)
    def add(a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c
    
calc = MultiCalculator()
print(calc.add(1, 2))
print(calc.add(1, 2, 3))

    
