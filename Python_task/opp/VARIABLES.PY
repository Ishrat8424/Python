# a=10
# def fun():
#     print(a)
#     b=20
#     print(b)
# def fun1():
#     print(a)
#     c=30
#     print(c)
# print(a)
# fun()
# # print(b)
# fun1()
# # print(c)
# print(a)



# a=10
# def fun():
#     # print(a)  UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
#     a=20
#     print(a)

# print(a)
# fun()
print("=============== modifying local veriable to global veriable =================================================")

# a=10
# def funn():
#     global a
#     a=100
#     print(a)
#     b=20
#     print(b)

# def funn1():
#     a=1000
#     print(a)
#     c=30
#     print(c)

# print(a)
# funn()
# funn1()
# print(a)


print(" ======== invoking the function using variable=========")
# def fun1():
#     print("fun1 invoked")

# def fun2(a,b):
#     c=a*b
#     print(c)

# print(fun1) #address of the function
# ptr1=fun1
# print(ptr1)
# ptr1()
# print(fun2)  #address of the function
# ptr2=fun2
# ptr2(10,5)

print("========== Passing the function as a parameter ========")
def fun1():
    print("function invoked")
def fun2(a,b):
    c=a*b 
    print(c)
def dis(ptr1,ptr2):
    ptr1()
    ptr2(10,5)
p1=fun1
p2=fun2
dis(p1,p2)
