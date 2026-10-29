def fibnocci(pos):
    n1,n2=0,1

    while pos>0:
        print(n1,end=" ")
        temp=n1+n2
        n1=n2
        n2=temp
        pos-=1


def incFibnocci(pos):
    n1,n2=0,1
    n=0
    while(n<pos ):
        print(n1,end=" ")
        temp=n1+n2
        n1=n2
        n2=temp
        n+=1

def decforfib(pos):
    n1,n2=0,1
    for i in range(pos,0,-1):
        print(n1,end=" ")
        temp=n1+n2
        n1=n2
        n2=temp

def incforfib(pos):
    n1,n2=0,1
    for i in range(0,pos):
         print(n1,end=" ")
         temp=n1+n2
         n1=n2
         n2=temp



pos=int(input("enter number:"))
fibnocci(pos)
print("\n===========================")
incFibnocci(pos)
print("\n===========================")
decforfib(pos)
print("\n===========================")
incforfib(pos)


