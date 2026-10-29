def palindrome(n,rev,temp):
   temp=temp
   if n<=0:
    return rev==temp
  
   digit=n%10
   rev=(rev*10)+digit
   n=n//10
   
   return palindrome(n,rev,temp)

n=int(input("Enter the numbre:"))
res=palindrome(n,0,n)
if res==True:
  print("It is a plindrome")
else:
  print("Not a palindrom")