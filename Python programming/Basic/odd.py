def evennum(series):
    return series % 2==0

n=int(input("enter the n :"))
series=0
while(n>0):
    if not evennum(series):
        print(series)
        n-=1
    series+=1
