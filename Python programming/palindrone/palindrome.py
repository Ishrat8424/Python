def integerPalindrome(n):
    temp=n
    if n<0:
        n*=-1

    rev=0
    while(n>0):
        digit=n%10
        rev=(rev*10)+digit
        n=n//10

    if temp<0:
        rev*=-1    
    return rev==temp

# def integerPalindrome(n):
#     return revrse(n)

n=int(input("Enter the number: "))

if integerPalindrome(n):
    print("It is the Palindrome")
else:
    print("Not a Palindrome")   



