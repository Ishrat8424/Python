def binaryToDecimal(n):
    pow=0
    dec=0
    n=int(n)
    while n>0:
        base=n%10
        dec=dec+base*(2**pow)
        n=n//10
        pow=pow+1	    
    return dec

str=input()
total=0
l=len(str)
for i in range(0,l):
    for j in range(i,l):
        n=(str[i:j+1])
        total+=binaryToDecimal(n)
print(total)