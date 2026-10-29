def isPrime(n):
    count=0
    i=1
    while i*i<=n:
        if n%i==0:
            count+=1
            if i!=(n//i):
                count+=1
        i+=1
    return count==2

st=int(input("Enter the starting range:"))
ed=int(input("Enter the end range:"))
if st>ed:
    st,ed=ed,st
    
print("Prime number between",st,"and",ed,"are:")
for i in range(st,ed+1):
    if isPrime(i):
        print(i,end=" ")
