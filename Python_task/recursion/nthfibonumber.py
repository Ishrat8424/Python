def fibo(n):
    if n==1 or n==0:
        return n
    return (fibo(n-1)+fibo(n-2))

n=int(input("Enter the nth number: "))
print("The nth fibo series is :",fibo(n))