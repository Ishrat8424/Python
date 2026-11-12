# WAP to merge the given 2 descending sorted array in decending order itself
def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr

def mergdec(arr1,arr2):
    i,j=0,0
    n1=len(arr1)
    n2=len(arr2)
    res=[]
    for k in range(0,n1+n2):
        if i<n2 and j<n2:
            if arr1[i]>arr2[j]:
                res.append(arr1[i])
                i+=1
            else:
                res.append(arr2[j])
                j+=1
        else:
            if i<n1:
                res.append(arr1[i])
                i+=1
            if j<n2:
                res.append(arr2[j])
                j+=1
    return res

def mergdec1(arr1,arr2):
    i,j=0,0
    n2=len(arr2)
    while j<n2:
        if i<len(arr1):
            if arr2[j]>arr1[i]:
                arr1.insert(i,arr2[j])
                i+=1
                j+=1
            else:
                i+=1
        elif j<n2:
            arr1.insert(i,arr2[j])
            j+=1


print("Enetr the 1st array")
arr1=intArray()
print("Enetr the 2nd array")
arr2=intArray()
res=mergdec(arr1,arr2)
print(res)
mergdec1(arr1,arr2)
print(arr1)