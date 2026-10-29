def isPrime(n,i,count):
    if i*i>n:
        return count==2

    if n%i==0:
        count+=1
    
        if i!=(n//i):
            count+=1
                
    return isPrime(n,i+1,count)


def facto(n,i):
    if i*i>n:
        return 
    if n%i==0:
        print(i,end=" ")
        if i!=(n//i):
            print(n//i,end=" ")
                
    facto(n,i+1)

def countfact(n,i,count):
    if i*i>n:
        return count
    if n%i==0:
        count+=1
    
        if i!=(n//i):
            count+=1
                
    return countfact(n,i+1,count)



n=int(input("enter the number"))
facto(n,1)
res=countfact(n,1,0)
print("\nthe number of factors in",n,"are:",res)

if isPrime(n,1,0):
    print("It is prime number:")
else:
    print("not a prime number ")

