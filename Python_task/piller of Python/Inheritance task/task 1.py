class Person:
    def __init__(self):
        self.name="Ishrat"
        self.age=21
    def display_person(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        self.student_id="4mk34cso43"
        self.course="CSE"
    def display_student(self):
        Person.display_person(self)
        print("ST ID:",self.student_id)
        print("Cource:",self.course)

s=Student()
s.display_student()

