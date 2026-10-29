


totalMarks=0
passed=0
failed=0
distinction=0
firstClass=0
secondClass=0
higest_marks=0
lowestMarks=0
print("===== ONLINE EXAM ===== ")
for i in range(1,16):
    print("\nEnter marks for Student",i,": ",end="")
    marks=int(input())
#--------------------------------------------------------
    while marks < 0 or marks > 100:
        print("Invalid Marks!")
        marks = int(input("Enter marks again: "))
#--------------------------------------------------------
    if i==1:
        higest_marks=marks
        lowestMarks=marks
    elif marks>higest_marks:
        higest_marks=marks
    elif marks<lowestMarks:
        lowestMarks=marks
#--------------------------------------------------------   
    if marks>=75 and marks<=100:
        classs="Distinction"
        distinction+=1
    elif marks<75 and marks>=60:
        classs="First Class"
        firstClass+=1
    elif 35<=marks and marks<=59:
        classs="Second Class"
        secondClass+=1
    elif marks>=0 and marks<=34:
        classs=" Fail"
#----------------------------------------------
    if marks>=0 and marks<=34:
        result="FAIL"
        failed+=1
    elif marks>=35 and marks<=100:
        result="PASS"
        passed+=1
#----------------------------------------------------
    totalMarks+=marks 
    print("Student",i,"Result:")
    print("\nMarks:",marks)
    print("Class:",classs)
    print("Result:",result)


print("\n\n===== FINAL REPORT ===== ")

print("\nTotal Students:",i)
print("Total Marks:",totalMarks)
print("Average Marks:",totalMarks/i)
print("Higest Marks:",higest_marks)
print("Lowest Marks :",lowestMarks)
print("Passed Students:",passed)
print("Failed Students:",failed)
print("Distinction Class:",distinction)
print("First Class:",firstClass)
print("Second Class:",secondClass)
