class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

    def display_name(self):
        print(f"Name: {self.name}")

class TA(Student): # TA is_a Student
    def __init__(self, name, grade, salary):
        super().__init__(name, grade)
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Salary: {self.salary}")

    def grade_student(self):
        print("grading student...")

class ClubMember(Student, ): # ClubMember is_a Student
    def __init__(self, name, grade, club):
        super().__init__(name, grade)
        self.club = club

    def display_info(self): # Override the display_info method to include club information
        super().display_info()
        print(f"Club: {self.club}")


Student1 = Student("A", 3.0)
TA1 = TA("B", 3.5, 2000)  
CM1 = ClubMember("C", 3.8, "Chess Club")

students = [Student1, TA1, CM1]
for student in students:    
    student.display_info()

for student in students:    
    student.display_name()

for student in students:    
    student.grade_student()