# •	WAP to display the first n integer palindromes
def isIntegerPalindrome(n):
    temp=n
    if n<0:
        n=n*-1
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10

    if temp<0:
        rev=rev*-1

    return rev==temp
num=int(input("enter how namy 1st n palindron you need: "))
n=num
series=1
while n>0:
    if isIntegerPalindrome(series):
        print(series,end=" ")
        n-=1
    series+=1