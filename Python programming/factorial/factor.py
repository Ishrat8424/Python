# def coluntfactors(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     return count
# n=int(input("enter the number>"))

# print("all the factors of ", n,"are: ")

# count=coluntfactors(n)
# print(count)



# def factors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=" ")
    
# n=int(input("enter the number>"))

# print("all the factors of ", n,"are: ")

# factors(n)

def coluntcycle(n):
    count=0
    for i in range(1,n+1):
        count+=1
        if n%i==0:
            continue

    return count

n=int(input("enter the number>"))
count=coluntcycle(n)
print("the number of cycle is ",count)



