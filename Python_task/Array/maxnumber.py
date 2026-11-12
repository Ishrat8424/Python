def intArray():
    arr=[]
    try:
        while True:
            n=int(input("Enter the number:"))
            arr.append(n)
    except Exception as e:
        return arr
# def arrnax(arr):
#     i=0
#     x=len(arr)
#     j=arr[x-1]
#     while(i<j):
#         if arr[i]>arr[j]:
#             max=arr[i]
#         else:
        
#             max=arr[j]
#         j-=1
#         i+=1
#     return max
def minnumber(arr):
    minele=2**31
    minindex=-1
    for i in range(0,len(arr)):
        if arr[i]<minele:
            minele=arr[i]
            minindex=i
    return minele,minindex



def maxnumberf(arr):
    maxele=-2**31
    maxinde=-1
    for i in range(0,len(arr)):
        if arr[i]>maxele:
            maxele=arr[i]
            maxinde=i
    return maxele,maxinde

print("Enter the numbers you want to enter....")
arr=intArray()
print("The number present in the array:...")
print(arr)
maxele,maxinde=maxnumberf(arr)
print("The maximum number in the array is:",maxele)
print("The index of the maximum number is:",maxinde)
minele,mininde=minnumber(arr)
print("The minimum number in the array is:",minele)
print("The index of the minimun number is:",mininde)

