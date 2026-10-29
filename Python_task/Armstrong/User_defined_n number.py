# WAP to display the first n Armstrong number

def count(n):
    c=0
    while n>0:
        n=n//10
        c+=1
    return c
#---------------------------------------
def isAmstrong(n):
    temp=n
    if n<0:
        n=n*-1

    pow=count(n)
    ans=0
    while n>0:
        digit=n%10
        ans=ans+(digit**pow)
        n=n//10

    if temp<0:
        ans=ans*-1
    return ans==temp
#----------------------------------------
n=int(input("enter the number of ASM number you need:"))
series=1
while n>0:
    if isAmstrong(series):
        print(series,end=" ")
        n-=1
    series+=1
