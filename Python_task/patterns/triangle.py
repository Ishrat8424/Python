#-------RHS inverted right angle triangle -----------
n =int(input("enter the num:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

#------------------------------------------------------
n =int(input("enter the num:"))
for i in range(n,1-1,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()

# -------LHS inverted right angle triangle -----------
n =int(input("enter the num:"))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*",end="")
    print()

#--------RHS Right Angle triangle--------
n =int(input("enter the num:"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


##RHS RIGHT ANGLE TRIANGLE 
n =int(input("enter the num:"))
for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
