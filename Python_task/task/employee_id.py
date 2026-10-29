class Employee:
    company_name="Kaizentrix Global Solution"
    emp_count=1000
    def __init__(self,name,department):    
        self.employee_name=name
        self.department=department

    def generate_employee_id(self):   
        Employee.emp_count+=1
        employee_id="EMP"+ str(self.emp_count)
        return employee_id

n=int(input("Enter the numbers of employee:"))
if n>0:
    employ=[ ]
    for i in range(1,n+1):
       print("Enter the details of",i,"Employee:")
       name=input("Enter the name:")
       dept=input("Enter the Dept:") 
       print("\n")
       emp=Employee(name,dept)
       employ.append(emp)

    print("The ",n,"employee Details are ")
    for emp in employ:
        print("------------------------------------------------")
        print("companey:",emp.company_name)
        print("Employee ID:",emp.generate_employee_id())
        print("Name:",emp.employee_name)
        print("Department:",emp.department)
   

else:
    print("Enter positive count")





