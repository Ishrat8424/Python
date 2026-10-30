def linearsearch(arr,target):
    for i in range(0,len(arr)):
        if target==arr[i]:
            return True
    return False

def linearsearchInd(arr,target):
    for i in range(0,len(arr)):
        if target==arr[i]:
            return i
    return -1


arr=[1,45,23,48,12,74,46,10,22,10]
target=int(input("Enter the target elememt"))
resint=linearsearchInd(arr,target)
if linearsearch(arr,target):
    print("element found at index",resint)
else:
    print("enement not found")