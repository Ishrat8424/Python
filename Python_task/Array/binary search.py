def intArray():
    ress=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            ress.append(n)
    except Exception as e:
        return ress

def binarysearch(arr,target):
    start=0
    end=len(arr)
    while start<end:
        mid=(start+end)//2

        if target==arr[mid]:
            return mid

        if target<arr[mid]:
            end=mid-1
        else:
            start=mid+1

    return -1

print("enter the elements:")
arr=intArray()
target=int(input("enter the target elements:"))
resind=binarysearch(arr,target)
if resind!=-1:
    print(target,"found at index",resind)
else:
    print(target,"is not found")