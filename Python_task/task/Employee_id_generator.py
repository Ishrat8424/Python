class Employee:
    comp_name="Kaizentrix Global Solution"
    emp_count=1000
    def __init__(self,name,department):    
        self.emp_name=name
        self.dept=department

    def emp_generateid(self):   
        Employee.emp_count+=1
        employee_id="EMP"+ str(self.emp_count)
        return employee_id

# for i in range(1,4):
emp1=Employee("Ishrat","CSE")
emp2=Employee("Jahan","ISE")
emp3=Employee("Khazi","kSE")

print("------------------------------------------------")
print("companey:",emp1.comp_name)
print("Name:",emp1.emp_name)
print("Department:",emp1.dept)
print("Emp_id:",emp1.emp_generateid())
print("-------------------------------------------------")

print("-------------------------------------------------")
print("companey:",emp2.comp_name)
print("Name:",emp2.emp_name)
print("Department:",emp1.dept)
print("Emp_id:",emp2.emp_generateid())
print("-------------------------------------------------")

print("-------------------------------------------------")
print("companey:",emp3.comp_name)
print("Name:",emp3.emp_name)
print("Department:",emp1.dept)
print("Emp_id:",emp3.emp_generateid())
print("--------------------------------------------------")