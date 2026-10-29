# WAP to reverse all the numbers present in a user defined range
def reverseNumber(n):
    temp=n
    if n<0:
        n=n*-1
    rev=0
    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        n=n//10
    
    if temp<0:
        rev=rev*-1
    return rev

st=int(input("enter the starting range:"))
ed=int(input("enter the starting range:"))

print("The reverse numbers are:")
for i in range(st,ed+1):
    print(reverseNumber(i),end=" ")