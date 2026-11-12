def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr

def reverseArr1(arr):
    res=[]
    for i in range(len(arr)-1,0-1,-1):
        res.append(arr[i])
    return res
def reversed2(arr):
    return list(reversed(arr))


def reversed3(arr):
    return arr[::-1]


def reverse4(arr):
    i=0
    j=len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

arr=intArray()
print(arr)
res=reverseArr1(arr)
print(res)
# print(arr)
res1=reversed2(arr)
print(res1)
res3=reversed3(arr)
print(res3)

res4=reverse4(arr)
print(arr)