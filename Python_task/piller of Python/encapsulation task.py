class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,salary):
        if salary<0:
            print("Invalid salary")
        else:
            self.__salary=salary

employee=Employee("ishrat",20000)

employee.set_salary(35000) 
print(employee.get_salary())


class Employee:
    def __init__(self):
        self.name=""
        self.__salary=""
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,salary):
        if salary<0:
            print("Invalid salary")
        else:
            self.__salary=salary

employee=Employee()

employee.set_salary(-35000) 
print(employee.get_salary())
          
