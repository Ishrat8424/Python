def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr

def secMax(arr):
    l=len(arr)
    me=2**31
    mei=-1
    sme=2**31
    smi=-1
    for i in range(0,l):
        if arr[i]<me:
            sme,smi=me,mei            
            me=arr[i]
            mei=i
        elif arr[i]!=me & arr[i]>me:
            sme=arr[i]
            smi=i
    return [me,mei,sme,smi]
arr=intArray()
res=secMax(arr)
print("minimum number:",res[0])
print("second minimum",res[2])