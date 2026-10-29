def reverse(n):
    temp=n
    if n<0:
        n*=-1

    rev=0
    while(n>0):
        digit=n%10
        rev=(rev*10)+digit
        n=n//10

    if temp<0:
        rev*=-1    
    return rev

n=int(input("Enter the number: "))
res=reverse(n)
print("the reverse of n is: ",res)