# def intArray():
#     arr=[]
#     try:
#         while True:
#             n=int(input("Enter the number:"))
#             arr.append(n)
#     except Exception as e:
#         return arr


# print("Enet the numbes you want to enter....")
# arr=intArray()
# print("The number present in the array:...")
# print(arr)



# arr=[]
# for i in range(5):
#     n=int(input("Enter the number:"))
#     arr.append(i,n)
# print(arr)


# arr=[]
# for i in range(5):
#     n=int(input("Enter the number:"))
#     arr.append(n)
# arr1=[]
# for i in arr:
#     if i%2==0:
#         arr1.append(i)
# for i in arr1:
#     print(i,end=" ")
# # print(arr1)

print("========== Filters ==================")
# def even(num):
#     return num%2==0
# l=[1,2,3,4,5,6,7,9]
# k=list(filter(even,l))
# print(k)

print("=============== lambda ============")
# k= lambda x,y:x+y
# r=k(10,5)
# print(r)

print("======== lambda and filter ==========")
# l=[1,2,3,4,5,6,8]
# k=list(filter(lambda x:x%2==0 ,l))
# print(k)

print("======== Maping ==========")
# def operation(n):
#     r=n+10
#     return r
# l=[1,2,3,4,5,6,7]
# k=list(map(operation,l))
# print(k)


print("======== Maping with lambda ==========")

# l=[1,2,3,4,5,6,7]
# k=list(map(lambda x:x+10,l))
# print(k)

print("=======temprature to celcius ========")
# l=[0,10,5,41,2,30]
# k=list(map(lambda x:x*(9//5)+32,l))
# print(k)

print("======== number grater than 10")
# l=[1,7,10,5,100,66,40,12,48,16,0,3]
# k=list(filter(lambda x:x>10,l))
# print(k)
# k=lambda x:x+2
# print(k(10))

def intArray():
    arr=[]
    while True:
        n=input("Enter the string:")
        if n=="":
            return arr
        arr.append(n)




print("Enet the numbes you want to enter....")
arr=intArray()
print("The number present in the array:...")
print(arr)

def chararray():
    l=[]
    while True:
        n=input("Enter the value:")
        if n=="":
            return l
        l.append(n[0])

arr=chararray()
print(arr)
