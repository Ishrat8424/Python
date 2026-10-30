# def indexoccrance(arr,target):
#     res=[-1,-1]
#     for i in range(0,len(arr)):
#         if target==arr[i]:
#             if res[0]!=-1:
#                 res[1]=i
#             else:
#                 res[0]=i
#                 res[1]=i
#     return res


# arr=[1,2,3,2,2,3,1,2]
# tar=int(input("Enter the target element:"))
# r=indexoccrance(arr,tar)
# print(r)

def indexoccrapointer(arr,target):
    res=[-1,-1]
    r=-1
    l=-1
    left=0
    right=len(arr)-1

    while left<=right:

        if target==arr[left]: 
            if res[0]==-1:
                res[0]=left
            else:
                l=left

        if arr[right]==target:
            if res[1]==-1:
                res[1]=right
            else:
                r=right  
             
        if res[0]!=-1 and res[1]!=-1:
            break

        left+=1
        right-=1

    if res[0]==-1 and left>right:
        res[0]=r

    if res[1]==-1 and left>right:
        res[1]=l
        
    if res[0]==-1 and res[1]!=-1:
        res[0]=res[1]
    if res[1]==-1 and res[0]!=-1:
        res[1]=res[0]
    return res


arr=[1,2,1,15,8,3,7,3]
tar=int(input("Enter the target element:"))
r=indexoccrapointer(arr,tar)
print(r)

