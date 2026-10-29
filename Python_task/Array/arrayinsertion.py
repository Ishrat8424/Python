arr=[]
print(arr)
print(len(arr))
arr.append(10)
arr.append(54)
arr.append("abcd")
print(arr)

arr.insert(2,333)
print(" =====")
arr.insert(-1,90)
print(arr)

arr[0]=1424
# arr[9]=12   IndexError: list assignment index out of range
print(arr)

arr1=[1,7,60]
arr2=[9,5,3]
arr1.append(arr2)
print(arr1)
arr1.insert(1,arr2)
print(arr1)
print("if i want to access or change the elememt present inside the arr2")
arr1[1][2]=55
print(arr1)

arr3=[7,8,4,5]
arr4=[55,88,66,33]
arr3.extend(arr4)
print(arr3)

arr5=[4,8,9,10,2]
arr5.insert[-1,250]
print(arr5)