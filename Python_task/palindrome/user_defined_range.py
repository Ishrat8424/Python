# WAP to display all the integer palindromes present in a user defined range 
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
#---------------------------------------------
st=int(input("enter the starting range:"))
ed=int(input("enter the starting range:"))

print("Palindrom af the number between",st,"and",ed,"are:")
for i in range(st,ed+1):
    if isIntegerPalindrome(i):
        print(i,end=" ")
