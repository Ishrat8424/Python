def isPrime(n):
    i=1
    count=0
    while i*i<=n:
        if n%i==0:
            count+=1
            if i!=(n//i):
                count+=1
        i+=1
    return count==2

num=int(input("enter the number:"))
if isPrime(num):
    print(num,"Is the Prime number")
else:
    print(num,"Is Not the Prime number")