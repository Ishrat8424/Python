def factors(n):
    arr=[]
    i=1
    while i*i<=n:
        if n%i==0:
            arr.append(i)
            if i!=n//i:
                arr.append(n//i)
        i+=1
    return arr

def isPrime(n):
    count=0
    i=1
    while i*i<=n:
        if n%i==0:
            count+=1
            if i!=n//i:
                count+=1
        i+=1
    return count==2
def maxnum(arr):
    max=-2**32
    n=len(arr)
    for i in range(0,n):
        if arr[i]>max:
            max=arr[i]

    return max
n=int(input("enter the number:"))
arr=factors(n)
print(arr)
pri=[]
for i in range(0,len(arr)):
    if isPrime(arr[i]):
        pri.append(arr[i])

print(pri)
larg=maxnum(pri)
print("Maximun prim factor",larg)
