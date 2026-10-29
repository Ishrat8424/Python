# def countnum(n,count):
#     if n<=0:
#         return count

#     # n=n//10
#     # count+=1
#     return countnum(n//10,count+1)

# n=int(input("enter the number:"))
# if n<0:
#     n*=-1
# res=countnum(n,0)
# print(res)

def countnum(n):
    if n<10:
        return 1

    return 1+countnum(n//10)

n=int(input("enter the number:"))
if n<0:
    n*=-1
res=countnum(n)
print(res)
