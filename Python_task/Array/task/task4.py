# 4. WAP to merge the given 2 ascending sorder array in decending order  

def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr

def mergedec(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=n1-1
    j=n2-1
    res=[]
    for k in range(0,n1+n2):
        if i>=0 and j>=0:
            if arr1[i]>arr2[j]:
                res.append(arr1[i])
                i-=1
            else:
                res.append(arr2[j])
                j-=1
        else:
            if i>=0:
                res.append(arr1[i])
                i-=1
            elif j>=0:
                res.append(arr2[j])
                j-=1

    return res


print("Enter the 1st array:")
arr1=intArray()

print("Enter the 2nd array:")
arr2=intArray()

print(arr1,arr2)
res=mergedec(arr1,arr2)
print(res)