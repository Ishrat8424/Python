class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def display(self):
        print("\nName\t:",self.name)
        print("Age\t:",self.age)
        print("course\t:",self.course)


obj1=Student("Ishrat",21,"CSE")
obj2=Student("Jahan",20,"ISE")
obj1.display()
obj2.display()