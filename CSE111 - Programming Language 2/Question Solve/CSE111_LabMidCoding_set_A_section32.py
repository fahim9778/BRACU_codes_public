class Person:
    def __init__(self):
        print("A new Person is born.")
        
    def personInfo(self, personObj):
        print(f"This person is a {personObj.personType}!")
        print(f"Name: {personObj.name}")
        print(f"ID: {personObj.ID}")
        print(f"Department: {personObj.department}")
        print(f"Department with all courses: {personObj.courses}")




p1 = Person()
print('##################')
st1 = Student('Bob', 1, 'CSE')
st1.addCourse('CSE110', 'CSE111')
p1.personInfo(st1)
print('--------------------------')
p2 = Person()
print('##################')
st2 = Student('Willie', 2)
st2.addCourse('MAT110', 'MAT120', 'PHY111', 'PHY112')
p1.personInfo(st2)
print('--------------------------')
st2.addDept('MNS')
print('--------------------------')
p3 = Person()
print('##################')
t1 = Teacher()
print('--------------------------')
print('Details of all the students:')
t1.allStudent(st1, st2)
