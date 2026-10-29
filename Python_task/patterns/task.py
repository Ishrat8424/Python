n= int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
print("==============================")
# * * * * 
# * * * * 
# * * * * 
# * * * * 

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i+j==n+1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("==============================")
# * * * * * 
# * *   * * 
# *   *   * 
# * *   * * 
# * * * * * 

for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end=" ")
    print()
# * * * * 
#  * * * * 
#   * * * * 
#    * * * *
print("==============================")

for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,n+1):
        if j==1 or i==1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()

for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end=" ")
    print()

print("==============================")
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("*",end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

print("==============================")
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

print("==============================")
noc=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(j,end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1


print("==============================")
noc=n
for i in range(1,n*2):
    for k in range(1,noc):
        print(" ",end=" ")
    for j in range(n,noc-1,-1):
        print(j,end=" ")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1

#       4 
#     4 3 
#   4 3 2 
# 4 3 2 1 
#   4 3 2 
#     4 3 
#       4 


print("==============================")

count=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
print("==============================")

noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print(j,end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

#    1 
#   1 2 
#  1 2 3 
# 1 2 3 4 
#  1 2 3 
#   1 2 
#    1 
print("==============================")

for i in range(1,n+1):
    for j in range(1,i*2):
        if i>=j:
            print(j,end="")
            k=j
        else:
            print(k-1,end="")
            k-=1
    print()
# 1
# 121
# 12321
# 1234321
print("==============================")

for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2!=0:
            print("1",end="")
        else:
            print("0",end="")
    print()

# 1
# 10
# 101
# 1010
# 10101
print("==============================")

# 1 2 3 4 5 4 3 2 1  
# 2 3 4 5 4 3 2  
# 3 4 5 4 3  
# 4 5 4  
# 5 

for i in range(1,n+1):
    for j in range(i,n*2-i+1):
        if j<=n:
            print(j,end="")
            k=j
        else:
            k-=1
            print(k,end="")          
    print()

# 1234321
# 23432
# 343
# 4

print("==============================")
for i in range(n,1-1,-1):
    for j in range(1,n+1):
        if i<j:
            print(i,end="")
        else:
            print(1,end="")
    print()
print("==========pending=============")


noc=1
for i in range(1,n*2):
    k=i
    for j in range(noc,1-1,-1):
    
        print(k,end=" ")
        k+=i
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
# 1 
# 2 4 
# 3 6 9 
# 4 8 12 16 
# 5 10 15 20 25 
# 6 12 18 24 
# 7 14 21 
# 8 16 
# 9 

print("=========Alphabet Patterns:")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()
# A
# AB
# ABC
# ABCD
# ABCDE
# ABCDEF
print("==============================")
for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):
        if i>=j:
            print(chr(64+i),end=" ")
        else:
            print(chr(64+j),end=" ")
    print()
# E E E E E 
# E D D D D 
# E D C C C 
# E D C B B 
# E D C B A
print("==============================")
noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(chr(64+j),end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
# ABCDEF
# ABCDE
# ABCD
# ABC
# AB
# A
# AB
# ABC
# ABCD
# ABCDE
# ABCDEF
print("==============================")
count=n*2+2
for i in range(1,n+1):
    prnt=count-i+1
    for j in range(1,i+1):
        print(chr(prnt+64),end="")
        prnt+=1
        count-=1

    print()
# J
# HI
# EFG
# ABCD
print("==============================")
count=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2!=0:
            print(chr(64+count),end=" ")
            countdec=count
        else:
            print(chr(countdec+64),end=" ")
            countdec-=1
        count+=1
    print()
    countdec=countdec+1+i
# A 
# C B 
# D E F 
# J I H G 
# K L M N O 
print("==============================")
for i in range(1,n+1):
    for j in range(i,n+i):
        print(chr(64+j),end="")
    print()
# ABCDE
# BCDEF
# CDEFG
# DEFGH
# EFGHI
print("==============================")
noc=n
for i in range(n,1-1,-1):
    for j in range(1,n*2):
        if j<=i:
            print(chr(j+64),end="")
            dec=j
        elif j>=noc:
            print(chr(dec+64),end="")
            dec-=1
        else:
            print(" ",end="")
    print()
    noc+=1
# ABCDEFGGFEDCB
# ABCDEF FEDCBA
# ABCDE   EDCBA
# ABCD     DCBA
# ABC       CBA
# AB         BA
# A           A
print("==============================")
noc=n
nor=n
for i in range(1,n*2):
    for j in range(1,n*2):
        if j<=noc:
            print(chr(j+64),end="")
            dec=j
        elif j>=nor:       
            print(chr(dec+64),end="")
            dec-=1
        else:
            print(" ",end="")
    print()
    
    if i<n:
        noc-=1
        nor+=1
    else:
        noc+=1
        nor-=1


noc =n
nor =n
for i in range(1,n*2):
    x = 1
    for j in range(1,n*2):
        if j<=nor or j>=noc:
            print(chr(x+64)," ",end=" ")
        else:
            print("   ",end=" ")
        if j<n:
            x+=1
        else:
            x-=1
    print()

    if i < n:
        noc += 1
        nor -= 1
    else:
        noc -= 1
        nor += 1



