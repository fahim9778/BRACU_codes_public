class Midexam:
    def __init__(self):
        self.z,self.x,self.y = 4,5,9
    def methodA(self):
        all = [1,2]
        self.y = self.y + self.methodB(all[1])
        self.x = self.x + self.methodB(all, all[0])
        self.z = self.x + self.y + all[0] + all[1]
        print(self.x, self.y, self.z)
    def methodB(self, *args):
        if len(args) == 1:
            a= args[0]
            x, y = 8,2
            y = y + a+ x % 7
            x = x + self.y + a   
            self.x = y + x + self.z
            self.y = a + x + 2
            self.z= self.x + self.y
            print(self.x, self.y, self.z)
            return x
        else:
            b, a = args
            x = 0
            self.y = self.y + b[1]
            x = self.z + x + a
            self.z = self.z + x + self.y
            b[0] = self.y + b[1]
            x = a + x + 2
            print(self.x, self.y, self.z)
            return x

t3 = Midexam()
t3.methodA()
