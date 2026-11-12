def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr

    
def reverse4(arr,i,j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
def rotationleft(arr,k):
    n=len(arr)
    if k>=n:
        k=k%n
    reverse4(arr,0,k-1)
    reverse4(arr,k,n-1)
    reverse4(arr,0,n-1)


arr=intArray()
k=int(input("Enter the rotation:"))
rotationleft(arr,k)
print(arr)
