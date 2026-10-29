n=int(input("enter the number"))
for i in range(n,1-1,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()
# 4444
# 333
# 22
# 1



# n=int(input("enter the number"))
for i in range(n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
# 1
# 22
# 333
# 4444



# n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(i,end="")
    print()
# 1111
# 222
# 33
# 4



# n=int(input("enter the number"))
for i in range(n,0,-1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,n+1):
        print(i,end="")
    print()
#    4444
#   3333
#  2222
# 1111



# n=int(input("enter the number: "))
for i in range(n,0,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
        print(i,end="")
    print()
# 4444
#  3333
#   2222
#    1111



# n=int(input("enter the number"))
for i in range(n,1-1,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
# 1234
# 123
# 12    
# 1



# n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(i,1-1,-1):
        print(j,end="")
    print()
# 1
# 21
# 321
# 4321



# n=int(input("enter the number"))
noc=1
for i in range(1,n*2):
    for j in range(n,noc-1,-1):
        print(j,end="")
    print()
    if i<n:
        noc+=1
        
    else:
        noc-=1
# 4321
# 432
# 43
# 4
# 43
# 432
# 4321



# n=int(input("enter the number"))
noc=4
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(j,end="")
    print()
    if i<n:
        noc-=1    
    else:
        noc+=1
# 1234
# 123
# 12
# 1
# 12
# 123
# 1234


# n=int(input("enter the number"))
noc=4
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print(j,end="")
    print()
    if i<n:
        noc-=1    
    else:
        noc+=1
 # 1234
 #  123
 #   12 
 #    1
 #   12
 #  123
 # 1234


# n=int(input("enter the number"))
noc=1
for i in range(1,n*2):
    for j in range(noc,n+1):
        print(j,end="")
    print()

    if i<n:
        noc+=1    
    else:
        noc-=1

# 1234
# 234
# 34
# 4
# 34
# 234
# 1234


# n=int(input("enter the number"))
for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
# 4 4 4 4 
#  3 3 3 
#   2 2 
#    1 



# n=int(input("enter the number"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()

#    1
#   12
#  123
# 1234



# n=int(input("enter the number"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(i,1-1,-1):
        print(j,end="")
    print()

#    1
#   21
#  321
# 4321



# n=int(input("enter the number"))
noc=1
for i in range(1,n*2):
    for k in range(1,noc):
        print(" ",end="")
    for j in range(noc,n+1):
        print(j,end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
#  1234
#   234
#    34
#     4
#    34
#   234
#  1234

# n=int(input("enter the number"))
noc=n
for i in range(1,n*2):
    for k in range(noc,1,-1):
        print(" ",end="")
    for j in range(n,noc-1,-1):
        print(j,end=" ")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1

#    4 
#   4 3 
#  4 3 2 
# 4 3 2 1 
#  4 3 2 
#   4 3 
#    4 


# n=int(input("enter the number"))
noc=1
for i in range(1,n*2):
    for k in range(1,noc):
        print(" ",end="")
    for j in range( noc,n+1):
        print(j,end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
# 1234
#  234
#   34
#    4
#   34
#  234
# 1234


# n=int(input("enter the number"))
noc=1
for i in range(1,n*2):
    for j in range(noc,n+1):
        print(j,end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
# 1234
# 234
# 34
# 4
# 34
# 234
# 1234


# n=int(input("enter the number"))
# count=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(count,end="\t")
#         count+=1
#     print()



# n=int(input("enter the number :"))
count=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==0:
            print("*",end="\t")  
        else:
            print(count,end="\t")
        count+=1
    print()

# 1       2       3       4
# *       *       *       *
# 9       10      11      12
# *       *       *       *


# n=int(input("enter the number :"))
countInc=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2!=0:
            print(countInc,end="\t")  
            countDec=countInc
        else:
            print(countDec,end="\t")
            countDec-=1
        countInc+=1    
    print()
    countDec=countDec+n
# 1       2       3       4
# 8       7       6       5
# 9       10      11      12
# 16      15      14      13

# n=int(input("enter the number"))
for i in range(n+1):
    for j in range(1,i+1):
        if (i+j)%2 == 0:
            print("1",end="")
        else:
            print("0",end="")
    print()

# 1
# 01
# 101
# 0101

# n=int(input("enter the number"))
for i in range(n,0,-1):
    for j in range(i):
        if (i+j)%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()
# 10101
# 0101
# 101
# 01
# 1


# n=int(input("enter the number"))
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



# n=int(input("enter the number"))
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

# 1 
# 3 2 
# 4 5 6 
# 10 9 8 7 



# n=int(input("enter the number"))
count=(n*(n+1)//2)
for i in range(n,1-1,-1):
    for k in range(1,i+1):
        print(count,end=" ")
        count-=1
    print()

# 10 9 8 7 
# 6 5 4 
# 3 2 
# 1 




# n=int(input("enter the number"))
count=(n*(n+1)//2)
for i in range(1,n+1):
    if i%2==0:
        countinc=count-(n-i)
    for j in range(n,i-1,-1):
        if i%2!=0:
            print(count,end="")
        else:
            print(countinc,end="")
            countinc+=1
        count-=1
    print()
    # 10 9 8 7 
    # 4 5 6
    # 3 2
    # 1


# n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
# 0000
# 1111
# 0000
# 1111




# n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n:
            print("1",end="")
        else:
            print("0",end="")
    print()
# 1111
# 0000
# 0000
# 1111




# n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

# 0 1 0 1 
# 0 1 0 1 
# 0 1 0 1 
# 0 1 0 1 

# n=int(input("Enter the number:"))
noc=4
for i in range(1,n*2):
    for k in range(1,noc+1):
        if i%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")

    print()
    if i<n:
        noc-=1
    else:
        noc+=1

# 0 0 0 0 
# 1 1 1 
# 0 0 
# 1 
# 0 0 
# 1 1 1 
# 0 0 0 0 

# n=int(input("enter the number")) 
count=n*2+2
countinc=count
for i in range(1,n+1):
    for j in range(1,i+1):
        print(countinc,end=" ")
        countinc+=1
        count-=1
    print()
    countinc=count-i

# 10 
# 8 9 
# 5 6 7 
# 1 2 3 4


for i in range(1, n + 1):
    for k in range(n,i,-1):
        print(" ",end="")
    num = 1
    for j in range(1, i + 1):
        print(num, end=" ")
        num = num * (i - j) // j
    print()
