def happy(n):
    if n==1:
        return True
    elif n==4:
        return False
    sum=0
    while n>0:
        base=n%10
        sum+=base*base
        n=n//10
    return happy(sum)

n=int(input("enter the number:"))
if happy(n):
    print("its a happy number")
else:
    print("Not a")