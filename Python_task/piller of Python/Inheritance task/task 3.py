class Employee:
    def __init__(self):
        self.name="Ishrat"
        self.employee_id="EMP451"
        self.salary=100000 
    def display_employee(self):
        print("Name:",self.name)
        print("ID:",self.employee_id)
        print("Salary",self.salary)


class Developer(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.programming_language="JAVA"
    def  write_code(self):
        print("Programming language used by the developer:",self.programming_language)


class SeniorDeveloper(Developer):
    def __init__(self):
        Developer.__init__(self)
        self.experience="5 years"
    def review_code(self):
        print("code revieve details:")
        print("Experience:", self.experience)

SD=SeniorDeveloper()
SD.display_employee()
SD.write_code()
SD.review_code()