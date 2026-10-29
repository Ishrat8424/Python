#WAP to display all n ASn number 
def countingDidits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
 
def amstring(n):
    temp=n
    if n<0:         #for negative number
        n=n*-1

    pow=countingDidits(n)
    base=0
    ans=0
#claculating the an Armstrong number or not
    while n>0:
        base=n%10
        ans=ans+(base**pow)
        n=n//10
# if the original number was negative conver it to the negative it self
    if temp<0:
        ans*=-1
# return the value
    return ans==temp

count=int(input("Enter the num :"))

if count <= 0:
    print("Armstrong numbers are defined only for positive counts.")
else:
    series=1
    print("the ASN are")
    while(count>0):
        if amstring(series):
            print(series, end=" ")
            count-=1
        series+=1
    
        
