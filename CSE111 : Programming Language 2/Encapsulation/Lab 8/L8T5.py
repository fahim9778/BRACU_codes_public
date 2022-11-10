class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"

class ScienceExam(Exam):
    def __init__(self,marks, time, *subjects):
        super().__init__(marks)
        self.time = time
        self.subjects = subjects
        self.subject_count_starts = 2
    def examSyllabus(self):
        return f"{super().examSyllabus()} , {self.subjects}"
    def examParts(self):
        examParts = super().examParts()
        for subject in self.subjects:
            self.subject_count_starts += 1
            examParts += f"Part {self.subject_count_starts} - {subject}\n"
        return examParts
    def __str__(self):
        return f"Exam Syllabus : {self.examSyllabus()}\nExam Parts : {self.examParts()}\nExam Time : {self.time}\nExam Marks : {self.marks}"
    

engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')