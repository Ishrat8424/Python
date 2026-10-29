# def recurssion(n):
#     if n>0:#base condition
#         print(n,end=" ")
#         recurssion(n-1)
#         return
#     else:
#         return

# n=int(input("enter the number:"))
# recurssion(n)

# def recurssion(n):
#     if n<=0:#base condition
#         return
        
#     else:
#         recurssion(n-1)
#         print(n,end=" ")
#         return

# n=int(input("\n enter the number:"))
# recurssion(n)

# def recurssion(n):
#     if n<=0:#base condition
#         return

        
#     print(n,end=" ")
#     recurssion(n-1)
#     if n!=1:
#         print(n,end=" ")
    

# n=int(input("\n enter the number:"))
# recurssion(n)
def display(n,i):
    if i>n:
        return 
    print(i,end=" ")
    display(n,i+1)
    print(i,end=" ")


num = int(input("Enter a number: "))
display(num,1)


