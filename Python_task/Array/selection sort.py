def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr


def selectionsortinc(arr):
    n=len(arr)
    for i in range(0,n-1):
        actualindex=n-1-i
        curmaxele,curmaxind=-2**31,-1
        for j in range(0,n-i):
            if arr[j]>curmaxele:
                curmaxele=arr[j]
                curmaxind=j
        maxeleindex=curmaxind
        arr[actualindex],arr[maxeleindex]=arr[maxeleindex],arr[actualindex]        
        

def selectionsortdec(arr):
    n=len(arr)
    for i in range(0,n-1):
        actualindex=n-1-i
        curminele,curminind=2**31,-1
        for j in range(0,n-i):
            if arr[j]<curminele:
                curminele=arr[j]
                curminind=j
        mineleindex=curminind
        arr[actualindex],arr[mineleindex]=arr[mineleindex],arr[actualindex]



print("Enter the elements :")
arr=intArray()
print("The entered number are:",arr)
print("array element after sorting in ascending order:")
selectionsortinc(arr)
print(arr)
print("array element after sorting in ascending order:")
selectionsortdec(arr)
print(arr)
