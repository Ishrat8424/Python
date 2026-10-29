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

num=int(input("Enter the range:"))

series=1
while num>0:
    if not isPrime(series):
        print(series,end=" ")
        num-=1

    series+=1