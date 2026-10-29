n=int(input("Enter the number:"))
decodd=n*2-1
incodd=1
for i in range(1,n+1):
    x=i
    for j in range(1,n+1):       
        if j%2!=0:
            print(x,end=" ")
            x=x+decodd
        else:
            print(x,end=" ")
            x=x+incodd  
    print()
    decodd=decodd-2
    incodd=incodd+2
print("=============================")
# Enter the number4
# 1 8 9 16 
# 2 7 10 15 
# 3 6 11 14 
# 4 5 12 13 




# n=int(input("Enter the number:"))
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



deodd=n*2-1
inodd=1
for i in range(1,n+1):
    x=i
    for j in range(1,i+1):
        if j%2!=0:
            print(x,end=" ")
            x=x+deodd
        else:
            print(x,end=" ")
            x=x+inodd
    print()
    deodd=deodd-2
    inodd=inodd+2
print("=============================")
# 1 
# 2 7 
# 3 6 11 
# 4 5 12 13





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