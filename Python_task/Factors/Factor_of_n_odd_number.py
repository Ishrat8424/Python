#LOGIC 1
def isFact(n):
    temp=n
    print("\n The factors of",n,"are:",end=" ")
    for i in range(1,temp+1):
        if n%i==0:
            print(i,end=" ")

#LOGIC 2
# def isFact(n):
#     temp=n
#     i=1
#     print("\n The factors of", n ,"is:",end=" ")
    
#     while i*i<=n:
#         if n%i==0:
#             print(i,end=" ")
#             if i!=(n//i):
#                 print(n//i,end=" ")
#         i+=1

num=int(input("Enter the range:"))
series=1
# temp=num
while num>0:
    if series%2!=0:
        isFact(series)
    series+=1
    num-=1

