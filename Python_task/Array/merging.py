def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr

    
def merg1(arr1,arr2):
    res=arr1+arr2
    return res

def merge2(arr1,arr2):
    arr1.extend(arr2)


def merge3(arr1,arr2):
    for i in arr2:
        arr1.append(i)
    
def merger4(arr1,arr2):
    for i in arr2:
        arr1.insert(len(arr1),i)

print("Enter the 1st array")
arr1=intArray()
print("Enter the 2nd array")
arr2=intArray()
print("Created Array 1:",arr1)
print("Created Array 1:",arr2)
res=merg1(arr1,arr2)
# print(arr1)
# print(arr2)
print(res)
print("-----------------------------------------------")
merge2(arr1,arr2)
print(arr1)
print("-----------------------------------------------")
merge3(arr1,arr2)
print(arr1)

print("-----------------------------------------------")
merger4(arr1,arr2)
print(arr1)
