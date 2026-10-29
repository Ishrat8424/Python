class Employee:
    company="KGS"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("\nName\t:",self.name)
        print("Salary\t:",self.salary)
        print("Companey:",Employee.company)

n=int(input("Enter the number of Employee:"))
list=[]
for i in range(n):
    print("\nEnter the details of",i,"Employee:")
    name=input("Enter the name:")
    salary=input("Enter the salary:")
    emp=Employee(name,salary)
    list.append(emp)

print("\nThe employee details")
for emp in list:
    emp.display()


