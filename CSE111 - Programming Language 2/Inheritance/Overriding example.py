class Bird:
    def fly(self):
        print("Bird is flying")

class Eagle(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

e = Eagle()
e.fly()

p = Penguin()
p.fly()

help(p)