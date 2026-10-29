# WAP to reverse all the numbers present in a user defined range display odd and even separaten
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

print("The enen reverse numbers are:")
for i in range(st,ed+1):
    if i%2==0:
        print(reverseNumber(i),end=" ")

print("\n The odd reverse numbers are:")
for i in range(st,ed+1):
    if not i%2==0:
        print(reverseNumber(i),end=" ")