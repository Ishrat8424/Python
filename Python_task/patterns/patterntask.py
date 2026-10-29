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

if n%2==0:
    n=n+1
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
print("==============================")
# * * * * 
#  * * * * 
#   * * * * 
#    * * * *

n= int(input("enter the number:"))
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,n+1):
        if j==1 or i==1 or i==n or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("==============================")
# * * * * 
#  *     * 
#   *     * 
#    * * * * 


for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end=" ")
    print()
print("==============================")
#    * * * * 
#   * * * * 
#  * * * * 
# * * * * 


for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,n+1):
        if j==1 or i==1 or i==n or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("==============================")
# * * * * * 
#  *       * 
#   *       * 
#    *       * 
#     * * * * * 


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

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 


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
print("==============================")
#     * 
#    * * 
#   *   * 
#  *     * 
# *       * 
#  *     * 
#   *   * 
#    * * 
#     * 




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
# *     *
# **   **
# *** ***
# *******
# *** ***
# **   **
# *     *


noc=1
nor=n*2-1
for i in range(1,n*2):
    for j in range(1,n*2):
        if j==1 or j==i or i+j==n*2 or j==n*2-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print("==============================")
# *       *
# **     **
# * *   * *
# *  * *  *
# *   *   *
# *  * *  *
# * *   * *
# **     **
# *       *

print("============ NUMBER PATTERNS ==================")
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
# 1
# 12
# 123
# 1234
# 123
# 12
# 1


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
print("==============================")
#       4 
#     4 3 
#   4 3 2 
# 4 3 2 1 
#   4 3 2 
#     4 3 
#       4 



count=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()
print("==============================")
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10



for i in range(0,n):
    for k in range(i,n-1):
        print(" ",end="")
    num = 1
    for j in range(0, (i+1)):
        print(num, end=" ")
        num = (num * (i - j)) // (j+1)
    print()
print("==============================")
#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 
# 1 4 6 4 1 


for i in range(1,n+1):
    for j in range(1,i*2):
        if i>=j:
            print(j,end="")
            k=j
        else:
            print(k-1,end="")
            k-=1
    print()
print("==============================")
# 1
# 121
# 12321
# 1234321


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
print("==============================")
#    1 
#   1 2 
#  1 2 3 
# 1 2 3 4 
#  1 2 3 
#   1 2 
#    1 



for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2!=0:
            print("1",end="")
        else:
            print("0",end="")
    print()
print("==============================")
# 1
# 10
# 101
# 1010
# 10101



for i in range(1,n+1):
    for j in range(n,0,-1):
        if i<j:
            print(1,end=" ")
        else:
            print(i,end=" ")
    print()
print("==============================")
# 1 1 1 1 1 
# 1 1 1 2 2 
# 1 1 3 3 3 
# 1 4 4 4 4 
# 5 5 5 5 5 



for i in range(1,n+1):
    for j in range(i,n*2-i+1):
        if j<=n:
            print(j,end="")
            k=j
        else:
            k-=1
            print(k,end="")          
    print()
print("==============================")
# 123454321
# 2345432
# 34543
# 454
# 5


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
print("==============================")
# 1 
# 2 4 
# 3 6 9 
# 4 8 12 16 
# 5 10 15 20 25 
# 6 12 18 24 
# 7 14 21 
# 8 16 
# 9 

print("====Alphabet Patterns======")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()
print("==============================")
# A
# AB
# ABC
# ABCD
# ABCDE
# ABCDEF


for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):
        if i>=j:
            print(chr(64+i),end=" ")
        else:
            print(chr(64+j),end=" ")
    print()
print("==============================")
# E E E E E 
# E D D D D 
# E D C C C 
# E D C B B 
# E D C B A



noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(chr(64+j),end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
print("==============================")
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


count=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2!=0:
            print(count,end=" ")
            countdec=count
        else:
            print(countdec,end=" ")
            countdec-=1
        count+=1  
    print()
    countdec=countdec+i+1
print("==============================")
# 1 
# 3 2 
# 4 5 6 
# 10 9 8 7 
# 11 12 13 14 15 



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
    countdec=countdec+i+1
print("==============================")
# A 
# C B 
# D E F 
# J I H G 
# K L M N O

deodd=n*2-1
inodd=1
for i in range(1,n+1):
    x=i
    for j in range(1,i+1):
        if j%2!=0:
            print(chr(x+64),end=" ")
            x=x+deodd
        else:
            print(chr(x+64),end=" ")
            x=x+inodd
    print()
    deodd=deodd-2
    inodd=inodd+2
print("=============================")
# A 
# B I 
# C H M 
# D G N Q 
# E F O P Y

count=n*2+2
for i in range(1,n+1):
    prnt=count-i+1
    for j in range(1,i+1):
        print(chr(prnt+64),end="")
        prnt+=1
        count-=1

    print()
print("==============================")
# J
# HI
# EFG
# ABCD



decodd=n*2-1
incodd=1
for i in range(1,n+1):
    x=i
    for j in range(1,n+1):       
        if j%2!=0:
            print(chr(64+x),end=" ")
            x=x+decodd
        else:
            print(chr(64+x),end=" ")
            x=x+incodd  
    print()
    decodd=decodd-2
    incodd=incodd+2
print("=============================")
# A J K T U 
# B I L S V 
# C H M R W 
# D G N Q X 
# E F O P Y 


# n=int(input("enter the number"))

noc =n
nor =n
for i in range(1,n*2):
    x = 1
    for j in range(1,n*2):
        if j<=nor or j>=noc:
            print(chr(x+64),end=" ")
        else:
            print(" ",end=" ")
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
print("==============================")
# A B C D E F E D C B A 
# A B C D E   E D C B A 
# A B C D       D C B A 
# A B C           C B A 
# A B               B A 
# A                   A 
# A B               B A 
# A B C           C B A 
# A B C D       D C B A 
# A B C D E   E D C B A 
# A B C D E F E D C B A 





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
print("==============================")
# ABCDEFGGFEDCB
# ABCDEF FEDCBA
# ABCDE   EDCBA
# ABCD     DCBA
# ABC       CBA
# AB         BA
# A           A


for i in range(1,n+1):
    for j in range(i,n+i):
        print(chr(64+j),end="")
    print()
print("==============================")
# ABCDE
# BCDEF
# CDEFG
# DEFGH
# EFGHI


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
print("==============================")
# A 
# C B 
# D E F 
# J I H G 
# K L M N O 


