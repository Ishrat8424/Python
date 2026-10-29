#----inverted pyramid---------
n =int(input("enter the num:"))
for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# * * * * 
#  * * * 
#   * * 
#    * 




n =int(input("enter the num:"))
for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i*2):
        print("*",end="")
    print()
# *******
#  *****
#   ***
#    *




n=int(input("enter the num:"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,(i*2-1)+1):
        print("*",end="")
    print()
#    *
#   ***
#  *****
# *******



n=int(input("enter the num:"))
noc=1
for i in range(1,n*2+1):

    for j in range(1,noc+1):
        print("*",end=" ")    
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
# * 
# * * 
# * * * 
# * * * * 
# * * * 
# * * 
# * 




n=int(input("enter the num:"))
noc=1
for i in range(1,n*2+1):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("*",end="")
    
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
#    *
#   **
#  ***
# ****
#  ***
#   **
#    *



n=int(input("enter the num:"))
noc=1
for i in range(1,n*2+1):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("*",end=" ")
    
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

#    * 
#   * * 
#  * * * 
# * * * * 
#  * * * 
#   * * 
#    * 



n =int(input("Enter the numbetr:"))
noc=1
for i in range(1,(2*n)):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,(noc*2)):
        print("*",end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *



#-----  RHS Parallelogram  -------
n=int(input("entwr the number:"))

for i in range(1,n+1):
    for k in range(i,n):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()

#    ****
#   ****
#  ****
# ****



#-----------LHS Parallelogram ----------
n=int(input("entwr the number:"))

for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()

# ****
#  ****
#   ****
#    ****




#======== k pattern=============
n=int(input("Enter the number:"))
noc=n
for i in range(1,2*n):
    for j in range(1,noc+1):
        print("*",end="")
    print()
    if i>=n:
        noc+=1
    else:
        noc-=1

# ****
# ***
# **
# *
# **
# ***
# ****



#============ inverted K============
n=int(input("Enter the number:"))
noc=n
for i in range(1,2*n):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("*",end="")
    print()
    if i>=n:
        noc+=1
    else:
        noc-=1
# ****
#  ***
#   **
#    *
#   **
#  ***
# ****



n=int(input("Enter the number:"))
noc=n
for i in range(1,2*n):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("*",end=" ")
    print()
    if i>=n:
        noc+=1
    else:
        noc-=1
# * * * * 
#  * * * 
#   * * 
#    * 
#   * * 
#  * * * 
# * * * * 




n=  int(input("Enter the number:"))
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,(noc*2)):
        print("*",end="")
    print()
    if i>=n:
        noc+=1
    else:
        noc-=1
# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******


 
n=int(input("Enter the number:"))
noc=(n*2)-1
for i in range(1,n+1):
    for j in range(1,n*2):
        if j<=i or j>=noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    noc-=1

#  *     *
#  **   **
#  *** ***
#  *******



 
n=int(input("Enter the number:"))
noc=n
for i in range(n,0,-1):
    for j in range(1,n*2):
        if j <= i or j >= noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    noc+=1

# *******
# *** ***
# **   **
# *     *



n=int(input("Enter the number:"))
noc=n*2-1
ref=1
for i in range(1,n*2):

    for j in range(1,n*2):
        if j <= ref or j >= noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i>=n:
        noc+=1
        ref-=1
    else:
        noc-=1
        ref+=1
# *     *
# **   **
# *** ***
# *******
# *** ***
# **   **
# *     *