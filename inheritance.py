class Student:
    def __init__(self, name, grade):
        self.name = zip(name)
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


Student1 = Student("A", 3.0)
TA1 = TA("B", 3.5, 2000)  

TA1.display_info()
TA1.display_name()


