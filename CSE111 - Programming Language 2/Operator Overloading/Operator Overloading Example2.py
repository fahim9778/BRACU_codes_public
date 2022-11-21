class Bill:
    def __init__(self, x):
        self.value = x

    def __str__(self):
        return f"{self.value}"
    
    def __add__(self, other):
        if isinstance(other, int):
            return type(self)(self.value + other)
        return type(self)(self.value + other.value) #Bill(100+200)

    def __radd__(self, other):
        return type(self)(self.value + other)

    def __gt__(self, other):
        return self.value > other.value

    __add__ = __radd__

        
b1 = Bill(100)
b2 = Bill(200)
b3 = Bill(300)
b4 = Bill(400)
b5 = Bill(500)

print(b1 + b3 + b2 + b4 + b5) #200
print(b5 + 10)
print(10 + b5)

print(b3 > b1 > b2)
