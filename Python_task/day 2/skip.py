# Imagine processing a list of numbers where you want to skip negative values, but stop completely if you find a zero 
list=[1,8,4,-1,5,4,7,-7,6,1,0,4]
for i in range(0,len(list)):
    if list[i]==0:
        break
    elif list[i]<0:
        continue
    print(list[i])


#--------------------------------------------------------------

# Write a program to keep asking for a number until you enter a negative number.
# At the end, print the sum of all entered numbers. 

while True:
    n=int(input("enter the number:"))
    if n<0:
        break


#--------------------------------------------------------------

# Write a program to ask for a name until the user enters END. 
# Print the name each time. When you are done, print "I am done." 

while True:
    name=input("Enter the name:")
    if name=="END" or name=="end":
        print("I am DONE")
        break
    print(name)


#--------------------------------------------------------------

# Test Average problem:  
# • As long as there are more grades, add them to the total 
# • Divide the total by the number of courses (each grade is a course) 
# • Print the corresponding letter grade 
# • Stop when the user enters a negative grade 
total=0
i=0
while True:
    n=int(input("Enter the grade: "))
    if n<0:
        break
    i+=1
    total+=n

if i>0:
    average=total/i
    if average>90:
        print("A+")
    elif average>80:
        print("A")
    elif average>70:
        print("B+")
    elif average>60:
        print("B")
    else:
        print("F")


#--------------------------------------------------------------

# WAP to print the follow series. 
# 105  98  91 ……….7 
for i in range(105,6,-7):
    print(i)


#--------------------------------------------------------------

# WAP to display the difference of sum of first “n” odd numbers and first “n” even numbers.
n=int(input("Enter the number:"))
even=0
odd=0
for i in range(1,2*n+1):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i

print("even:",even)
print("odd",odd)
print("the difference is :",even-odd)


#--------------------------------------------------------------


# WAP to display all the numbers between the defined range using while loop.
st=int(input("enter the starting:"))
en=int(input("Enter the end:"))
i=st
while st<en:
    print(st,end=" ")
    st+=1


#--------------------------------------------------------------

# WAP to enter the numbers till the user wants and at the end it should display the sum of all the entered numbers. 
# The loop should work until the user enter 0. 
sum=0
while True:
    n=int(input("Enter the number:"))
    if n==0:
        break
    sum+=n

print("The sum of the numbers are:",sum)


#--------------------------------------------------------------


# WAP to enter the numbers till the user enters 0 
# and at the end it should display the count of positive number and negative number separately. 
pos=0
neg=0
while True:
    n=int(input("Enter the number:"))
    if n==0:
        break
    elif n>0:
        pos+=n
    else:
        neg+=n

print("the sum of the positive number:",pos)
print("the sum of the negative number:",neg)


#--------------------------------------------------------------

# WAP to accept “n” random positive numbers from the user and display the largest and smallest out of it. 
num=int(input("Enter the input"))
for i in range(num):
    n=int(input("Enter the value:"))
    if i==0:
        largest=n
        smalest=n

    elif n>largest:
        largest=n
    elif n<smalest:
        smalest=n

print("larger is:",largest)
print("Smallest is:",smalest)



#--------------------------------------------------------------

# WAP to display first “n” values of the following series. 
# Eg:  N = 3  2  22  222   
# N = 5  2  22  222  2222  22222 

n=int(input(" Enter the n: "))
num=""
for i in range(1,n+1):
    num=num+"2"
    print(num,end=" ")


#--------------------------------------------------------------


# WAP to display natural even numbers starting from “n”. 
count=int(input("Enter the count of the number:"))
n=int(input("Enter the starting number:"))
# if n%2!=0:
#     n=n+1

while count>0:
    if n%2==0:
        print(n,end=" ")
        count-=1
    n+=1


#--------------------------------------------------------------

#  WAP to swap the numbers present in variables without using the 3rd variable or the standard predefined approach.
n1=int(input("enter the n1:"))
n2=int(input("Enter the n2: "))
print("Before swap the n ",n1)
print("Before swap the n2 ",n2)
n1=n1+n2
n2=n1-n2
n1=n1-n2
print("After swap the n1 ",n1)
print("After swap the n2 ",n2)


#--------------------------------------------------------------


# Keep asking the user for a password until they get it right, 
# but lock them out after 3 wrong Note: Let the curr_password be predefined. 
pas="Ishrat@2004"
for i in range(3):
    p=input("Enter the correct password:")
    if p==pas:
        print("correct password")
        break
    elif i==0:
        print("wrong passoward enter again only 2 attempt remaining...!")
    elif i==1:
        print("wrong passoward enter again only 1 attempt remaining...!")