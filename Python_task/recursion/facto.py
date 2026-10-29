def fact(n,i,):
    if i>n:
        return
    if n%i==0:
        print(i,end=" ")
    fact(n,i+1)


def factcount(n,i,count):
    if i>n:
        return count
    if n%i==0:
        count+=1
    return factcount(n,i+1,count)

n=int(input("ebter the number: "))
fact(n,1)
print("\n the number of factors are :")
print(factcount(n,1,0))