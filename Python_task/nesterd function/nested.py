# def outer():
#     print("Entering inner")
    
#     def inner():
#         print("Entering inner")
#         print("Processing")
#         print("calling inner")
#     inner()

# r=outer()

print("=========local to non local=======")
# def fun1():
#     a=10
#     print(a)
#     def fun2():
#         nonlocal a
#         a=100
#         print(a)
#     fun2()
#     print(a)
#     # print(b)

# fun1()
# fun1.fun2()
# from math import pi as a
print("========= L E G B Rule=======")
# # a=100
# def outer():
#     # a=15
#     def inner():
#         # a=10
#         print(a)
#     inner()
# outer()

print("=====closer=============")

def outer():
    print("Entering outer")
    
    def inner():
        print("Entering inner")
        print("Processing")
        print("calling inner")
    return inner

ref=outer()
print("\nleaving outer ref calling")
ref()