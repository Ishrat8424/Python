def calculate_salary(salary,HRA,DA):
    return salary+HRA+DA
sal=int(input("Enter the salary:"))
HRD=int(input("Enter the HRD:"))
DA=int(input("Enter the DA:"))
print("TOTAL SALARY:",calculate_salary(sal,HRD,DA))