# def gcd(n1,n2,lower,i,g):
#     if i>lower:
#         return g
#     if n1%i==0 and n2%i==0:
#         g=i
#     return gcd(n1,n2,lower,i+1,g)

def gcd(n1,n2):
    if n1==0:
        return n2
    if n1<n2:
        n1,n2=n2,n1
    return gcd((n1%n2),n2)
    

n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))

res=gcd(n1,n2)
print(res)