def fact(n):
    f=1
    while(n>0):
        f=f*n
        n=n-1

    return f

def strong(n,temp):
    st=0
    while(n>0):
        digit=n%10
        st=st+(fact(digit))
        n=n//10
    return temp==st

n=int(input("Enter the number:"))
if strong(n,n):
   print("It is a strong number")
else:
    print("It is not a strong number")