def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr

def merge(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    res=[]
    for k in range(0,n1+n2):
        if i<n1 and k%2==0:
            res.append(arr1[i])
            i+=1
        elif j<n2 and k%2!=0:
            res.append(arr2[j])
            j+=1
        else:
             if i<n1:
                  res.append(arr1[i])
                  i+=1
             elif j<n2:
                  res.append(arr2[j])
                  j+=1
    return res 

def merge2(arr1, arr2):
    n2 = len(arr2)

    i = 1
    j = 0

    while j < n2:
        if i <= len(arr1):
            arr1.insert(i, arr2[j])
            i += 2
        else:
            arr1.insert(i,arr2[j])
        j += 1
                 
                 


print("Enter array 1:")
arr1=intArray()
print("Enter array 2:")
arr2=intArray()
# print(arr1)
# print(arr2)
# res=merge(arr1,arr2)
# print(res)
merge2(arr1,arr2)
print(arr1)

