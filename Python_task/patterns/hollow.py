
n= int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("==============================================\n")
if n%2==0:
    n=n+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i+j==n+1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("==============================================\n")
if n%2==0:
    n=n+1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or i+j==n+1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("==============================================\n")
if n%2==0:
    n=n+1

for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or i+j==n+1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("==============================================\n")

for i in range(1,n+1):
    for k in range(n,i-1,-1):
        print(" ",end="")
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("==============================================\n")

for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("==============================================\n")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==1 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("==============================================\n")
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
    
        if j==1 or i==n or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("==============================================\n")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==1 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("==============================================\n")
for i in range(1,n+1):
    for k in range(n,i,-1):
        print("",end=" ")
    for j in range(1,i+1):
    
        if j==1 or i==n or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("==============================================\n")

for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        if i==j or i==n or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print("==============================================\n")

for i in range(n,i-i,-1):
    for k in range(n,i,-1):
        print("",end=" ")
    for j in range(1,i+1):
        if j==1 or i==n or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("==============================================\n")
noc=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        if j==1 or noc==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1


print("==============================================\n")
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end=" ")
    for j in range(1,noc+1):
        if j==1 or noc==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
print("==============================================\n")
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print("",end=" ")
    for j in range(1,noc+1):
        if j==1 or noc==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

print("==============================================\n")
noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        if j==noc or noc==n or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i <n:
        noc-=1
    else:
        noc+=1

print("==============================================\n")
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if j==noc or noc==n or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i <n:
        noc-=1
    else:
        noc+=1

print("==============================================\n")
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print("",end=" ")
    for j in range(1,noc+1):
        if j==noc or noc==n or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i <n:
        noc-=1
    else:
        noc+=1
print("==============================================\n")
noc=1
nor=n*2-1
for i in range(1,n*2):
    for j in range(1,n*2):
        if j==1 or j==i or i+j==n*2 or j==n*2-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("==============================================\n")
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print("",end=" ")
    for j in range(1,noc+1):
        if j==1 or noc==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1