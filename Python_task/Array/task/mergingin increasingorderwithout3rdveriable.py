def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr

    
def merge1(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i,j=0,0
    while j<n2:
        if i<len(arr1):
            if arr1[i]>arr2[j]:
                arr1.insert(i,arr2[j])
                j+=1
            else:
                i+=1