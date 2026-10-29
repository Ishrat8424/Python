def findHCF(n1,n2):
    lower=n1
    if n2<n1:
        lower=n2
    gcd=1
    for i in range(2,lower+1):
        if n1%i==0 and n2%i==0:
            gcd=i
    return gcd


num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
rec=findHCF(num1,num2)
print("the GCD of", num1, "and" ,num2," is:", rec)