class Student:
    schoolname = "BIU School" # Class Variable
    def __init__(self, name, roll):
        self.name = name        # Instance variable
        self.roll = roll        # Instance variable
    
    def printStudent(self):
        print("Name: ", self.name)
        print("Roll: ", self.roll)
        print("School Name: ", type(self).schoolname)


s1 = Student("Rahim", 101)
s2 = Student("Karim", 102)
s1.printStudent()
s2.printStudent()

Student.schoolname = "BRAC School"
print(s1.schoolname)
s1.printStudent()
s2.printStudent()