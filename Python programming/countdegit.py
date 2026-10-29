#count the number of degits present in a given number
def countingDidits(n):
    n=abs(n)
    count=0
    while n>0:
        n=n//10
        count+=1
    return count


n=int(input("enter the nuumber:"))
countt=countingDidits(n)
print("the count of digit is",countt)
