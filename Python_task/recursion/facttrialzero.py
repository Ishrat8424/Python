def factorial(n,fact):
    if n<=0:
        return fact
    fact*=n
    n=n-1
    return factorial(n,fact)

def trailingZeroes(num):
    fact=factorial(num,1)
    zero=0
    while fact>0:
        if fact%10==0:
            zero+=1
        else:
            break
        fact//=10
    return zero


num=int(input())
res=trailingZeroes(num)
print(res)


    # def trailingZeroes(self, n: int) -> int:
    #     if n<=0:
    #         return 0
    #     return n//5+self.trailingZeroes(n//5)
    # this is the optimised technique first find how many multiple of 5 are present (n//5)
    # then recurse the function again to (n=n//5)