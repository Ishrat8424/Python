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


def sumofprime(n):
    sum=0
    for i in range(n+1):
        if isPrime(i):
            sum+=i
    return sum

n=int(input("enter the num:"))
res=sumofprime(n)
print(res)