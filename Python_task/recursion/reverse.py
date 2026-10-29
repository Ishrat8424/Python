def reverse(n,rev):
   if n<=0:
    return rev
  
   digit=n%10
   rev=(rev*10)+digit
   n=n//10
   
   return reverse(n,rev)
    

n=int(input("enter the number:"))
res=reverse(n,0)
print(res)
