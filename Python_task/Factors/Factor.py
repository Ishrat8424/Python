# LOGIC 1
# def isFactor(n):
#     temp=n
#     print("\n The factors of",n,"are:",end=" ")
#     for i in range(1,temp+1):
#         if n%i==0:
#             print(i,end=" ")

#LOGIC 2
def isFactor(n):
    i=1
    while i*i<=n:
        if n%i==0:
            print(i,end=" ")
            if i!=(n//i):
                print(n//i,end=" ")
        i+=1

num=int(input("enter the number:"))
print("the factors are :")
isFactor(num)
