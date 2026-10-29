def reverseNumber(n):
    temp=n
    if n<0:
        n=n*-1
    rev=0
    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        n=n//10

    if temp<0:
        rev=rev*-1
    return rev

num=int(input("Enter the number to be reversed: "))
rev=reverseNumber(num)
print("the reverse of",num,"is:",rev)
