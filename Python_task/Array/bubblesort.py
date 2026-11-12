def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr

def biblesortacs(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
def biblesortdec(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]   

arr=intArray()
biblesortacs(arr)
print("ascending order",arr)
biblesortdec(arr)
print("descending order",arr)