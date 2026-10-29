#Write a program to check weather the given number is an Armstrong number or not 
def countingDidits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
 
def amstring(n):
    temp=n
    if n<0:         #for negative number
        n=n*-1

    pow=countingDidits(n)
    # base=0
    ans=0
#claculating the an Armstrong number or not
    while n>0:
        base=n%10
        ans=ans+(base**pow)
        n=n//10
# if the original number was negative conver it to the negative it self
    if temp<0:
        ans*=-1
# return the value
    return ans==temp

n=int(input("enter the nuumber:"))
if amstring(n):
    print("is a Armstrong number")
else:
    print("is not Armstrong number")
