#LOGIC 1
# def isFactor(n):
#     i=1
#     print("\n the factors of",n,"are:",end=" ")
#     while i*i<=n:
#         if n%i==0:
#             print(i,end=" ")
#             if i!=(n//i):
#                 print(n//i,end=" ")
#         i+=1


#LOGIC 2
def isFactor(n):
    print("\n the factors of",n,"are:",end=" ")
    i=1
    temp=n
    for i in range(1,temp+1):
        if n%i==0:
            print(i,end=" ")
        i+=1
    
st=int(input("Enter the starting range:"))
ed=int(input("Enter the ending range"))

if st>ed:
    st,ed=ed,st

if st>=0 and ed>0:
    print("The factors of the given range are:")
    for i in range(st,ed+1):
        isFactor(i)
else:
    print("Enter the positive range !!!!")