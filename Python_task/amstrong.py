def countnum(n,count):
    if n<=0:
        return count
    return countnum(n//10,count+1)

def amstrong(n,ans,pow,temp):
    if n<=0:
        return temp==ans

    base=n%10
    # ans=(ans+(base**pow))
    # n=n//10
    return amstrong(n//10,(ans+(base**pow)),pow,temp)



n=int(input("enter the number:"))
if n<0:
    n=n*-1
    
pow=countnum(n,0)
if amstrong(n,0,pow,n): 
    print("is a asn")
else:
    print("not a asn")