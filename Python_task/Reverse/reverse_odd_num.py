# WAP to reverse all the odd numbers present in a user defined range keep the even number as it is
def reverseOddNumber(n):
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
    if not i%2==0:
        print(reverseOddNumber(i),end=" ")
    else:
        print(i,end=" ")