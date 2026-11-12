class  Employee:
    def __init__(self):
        self.name="Ishrat"
        self.employee_id="UD012"
    def display_employee(self):
        print("Name:",self.name)
        print("ID:",self.employee_id)

class Skills:
    def __init__(self):
        self.skill="coding,Drading,debugging.."
    def display_skill(self):
        print("skills:",self.skill)

class Developer(Employee,Skills):
    def __init__(self):
        Employee.__init__(self)
        Skills.__init__(self)
        self.project="iot project" 
    def work(self):
        print("The project assigned is:",self.project)

D=Developer()
D.display_employee()
D.display_skill()
D.work()
