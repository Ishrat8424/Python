def iscoprome(n1,n2):
    lower=n1
    gcd=1
    if n2<n1:
        lower=n2
    for i in range(2, lower+1):
        if n1%i==0 and n2%i==0:
            gcd=i
    return gcd==1

num1=int(input("enter the first num:"))
num2=int(input("enter the second num:"))
if iscoprome(num1,num2):
    print("is a co prime number:")
else:
    print("is not a co prime number:")


    