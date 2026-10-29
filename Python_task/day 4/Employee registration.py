# Employee registration: Accept an employee's name and age, and keep asking for the age until it is between 18 and 60. 
# Let the user choose a department (Development, Testing, HR, or Sales), each with a different base salary. 
# Add an experience bonus (01 years: none, 2-4 years: Rs.7000, 5+ years: Rs.15000). Print the registration summary.

name=input("Enter Your Name: ")
ag=True
while ag:
    age=int(input("Enter Your Age: "))
    if age<18 or age>60:
        print("Invalid age...!")
    else:
        ag=False


while True:
    print("\n===== SELECT DEPARTMENT =====")
    print("1. Development - Rs.40000")   
    print("2. Testing     - Rs.30000")
    print("3. HR          - Rs.25000")
    print("4. Sales       - Rs.20000")
    choice = int(input("Choose Department (1-4): "))  
    if choice>=5:
        print("Invallid choice...!")
    else:
        break

salary=0
if choice==1:
    salary=40000
    dept="Development"
elif choice==2 :
    salary=30000
    dept="Testing"
elif choice==3:
    salary=25000
    dept="HR"
elif choice==4:
    salary=20000
    dept="Sales"

exp=int(input("Enter your Years of Experience:"))
bonas=0   
if exp<=1:
    bonas=0
elif exp>1 and exp<=2: 
    bonas=7000
elif exp>=5: 
    bonas=15000

print("\n\n======= EMPLOYEE REGISTRATION =======")
print("\nEmployee Name\t",":",name)
print("Employee Age\t",":",age)
print("Department\t",":",dept)
print("Experience\t",":",exp,"Year")
print("\nBase Salary\t",":Rs.",salary)
print("Experience Bonus",":Rs.",bonas)
print("-------------------------------------")
print("Final Salary\t",":Rs.",bonas+salary)
print("\nRegistration Successful!")
    