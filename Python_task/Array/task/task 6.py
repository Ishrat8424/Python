# 6. WAP to merge the given 2 decending sorted array in ascending order
def intArray():
    ress=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            ress.append(n)
    except Exception as e:
        return ress

def mergeasc(arr1,arr2):
    i,j=0,0
    n1=len(arr1)
    n2=len(arr2)
    for k in range(n1+n2):
        if arr1[]