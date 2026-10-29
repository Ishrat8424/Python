def fiboseries(pos,n1,n2):
    if pos<=0:
        return n1
    # print(n1,end=" ")
    return fiboseries(pos-1,n2,n1+n2)

n=int(input("enter the number: "))

res=fiboseries(n,0,1)
print(res)