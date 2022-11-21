# Public URL (for your students): https://codecheck.io/files/2211201322drltnf7wx2f4ajutpcescrrp8
# Edit URL (for you only): https://codecheck.io/private/problem/2211201322drltnf7wx2f4ajutpcescrrp8/51OFMWNTSY3IEUPYVI0G5WNCP

"""Design the Student class such a way so that the following code provides the expected output. 
Hint:
Write the constructor with appropriate default value for arguments.

Write the dailyEffort() method with appropriate arguments.

Write the printDetails() method. For printing suggestions check the following instructions.
If Negative hour, print "WAIT A MINUTE! NEGATIVE WORKING HOURS?!"
If Zero hour, then print "No effort today".
If 0 < hour <= 2 print 'Suggestion: Should give more effort!'
If 2 < hour <= 4 print 'Suggestion: Keep up the good work!'
Else print 'Suggestion: Excellent! Now motivate others.'
"""
class Student:
    ##HIDE
    def __init__(self, name, id, dept = "CSE"):
        self.name = name
        self.id = id
        self.dept = dept
        self.hour = 0
        self.suggestion = ""
    ##EDIT def __init__(. . .):
    
    def dailyEffort(self, hour):
        ##HIDE
        self.hour = hour
        # if hour < 0:
        #     self.suggestion = "WAIT A MINUTE! NEGATIVE WORKING HOURS?!"
        if hour == 0 :
            self.suggestion = "No effort today"
        elif hour <= 2:
            self.suggestion = "Suggestion: Should give more effort!"
        elif hour <= 4:
            self.suggestion = "Suggestion: Keep up the good work!"
        else:
            self.suggestion = "Suggestion: Excellent! Now motivate others."
        ##EDIT def dailyEffort(. . .):
    
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Department: {self.dept}")
        print(f"Daily Effort: {self.hour} hour(s)")
        print(f"{self.suggestion}")

# harry = Student('Harry Potter', 123) ##SUB Student("Ash Ketchum", 111, "Pokemon")
# harry.dailyEffort(3) ##SUB 3
# harry.printDetails()    
# print('========================')
# john = Student("John Wick", 456, "BBA")
# john.dailyEffort(2)
# john.printDetails()
# print('========================')
# naruto = Student("Naruto Uzumaki", 777, "Ninja")
# naruto.dailyEffort(-6)
# naruto.printDetails()
# print('========================')


# ## SOME ADDITIONAL HIDDEN TEST CASES MAY RUN TO JUSTIFY PROPER LOGIC
# ##HIDE
# ash = Student("Ash Ketchum", 111, "Pokemon")
# ash.dailyEffort(1)
# ash.printDetails()
# print('========================')
# mario = Student("Mario", 222, "Mario")
# mario.dailyEffort(5)
# mario.printDetails()
# print('========================')
# scooby = Student("Sooby Doo", 333)
# scooby.dailyEffort(0)
# scooby.printDetails()
# print('========================')