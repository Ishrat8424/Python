# WAP To display the all ams number and non-armstrong number in user defined range separately

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
st=int(input("enter the starting range:"))
ed=int(input("enter the starting range:"))
print("The ASM numbers")
for i in range(st,ed+1):
    if isAmstrong(i):
        print(i,end=" ")

print("\n The not ASM numbers")
for i in range(st,ed+1):
    if not isAmstrong(i):
        print(i,end=" ")

