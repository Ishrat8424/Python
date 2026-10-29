def sumofnum(n,sum):
    if n<=0:
        return sum
    return sumofnum(n-1,sum+n)

n=int(input())
print(sumofnum(n,0))