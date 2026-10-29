#user defined range 
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

st=int(input("Enter the range: "))
ed=int(input("Enter the end range: "))

for i in range(st,ed+1):
    res=reverse(i)
    print(res, end=" ")


