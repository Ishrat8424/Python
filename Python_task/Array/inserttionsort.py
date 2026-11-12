def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr

def insertionasc(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(i+1,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break

def insertiondes(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(i+1,0,-1):
            if arr[j-1]<arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break

arr=intArray()
insertionasc(arr)
print(arr)    
insertiondes(arr)
print(arr)      