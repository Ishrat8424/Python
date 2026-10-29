# def isprimw(n):
#     temp=n
#     i=1
#     count=0
#     while i*i <=n:
#         if n%i==0:
#             count+=1

#             if i!=(n//1):
#                 count+=1
#         i+=1
#     return count==2

# num=int(input("enter the number"))
# if isprimw(num):
#     print("is a prime nymber")
# else:
#     print("Not a prime number")


def isprime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count==2
    
n=int(input("enter the number: "))

print("all the factors of ", n,"are: ")

if isprime(n):
    print("is a prime number")
else:
    print("Not a prime number")