def pownum(x,n):
    if n==0:
        return 1
    
    return x*(pownum (x,n-1))

print (pownum(2,2))