def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr
def linearsearchpointer(arr,target):
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]==target:
            return i
        elif arr[j]==target:
            return j
        j-=1
        i+=1
    return -1

arr=intArray()
target=int(input("enter the target element:"))
index=linearsearchpointer(arr,target)
if index==-1:
    print("Element not found")
else:
    print("Array element found on inder",index)