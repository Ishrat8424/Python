def intArray():
    ress=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            ress.append(n)
    except Exception as e:
        return ress

def MergeSortMerging(arr,start,mid,end):
    res=[]
    i=start
    j=mid+1

    for k in range(0,(mid+end)+1):
        if i<=mid and j<=end:
            if arr[i]<arr[j]:
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j+=1
        else:
            if i<=mid:
                res.append(arr[i])
                i+=1
            elif j<=end:
                res.append(arr[j])
                j+=1

    for k in range(0,len(res)):
        arr[start]=res[k]
        start+=1

def mergeSortDivision(arr,start,end):
    if start>=end:
        return

    mid=(start+end)//2
    #LHS division
    mergeSortDivision(arr,start,mid)

    #RHS division
    mergeSortDivision(arr,mid+1,end)

    #Merging
    MergeSortMerging(arr,start,mid,end)


arr=intArray()
print("Array before sorting",arr)
mergeSortDivision(arr,0,len(arr)-1)
print("Sorted array",arr)