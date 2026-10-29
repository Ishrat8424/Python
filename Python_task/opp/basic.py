# data=(input("Enter the char:"))
# ascii=ord(data)
# print(ascii)
# data1=chr(ascii)
# print(data1)
# #======== Upper to lower==========
# data=(input("Enter the char:"))
# d=""
# for i in data:
#     if ord(i)>=65 and ord(i)<=90:
#         d=d+chr((ord(i)+32))
#     else:
#         d=d+i
# print(d)


# #======== Lower to Upper ==========
# data=(input("Enter the char:"))
# d=""
# for i in data:
#     if ord(i)>=97 and ord(i)<=122:
#         d=d+chr((ord(i)-32))
#     else:
#         d=d+i
# print(d)


#============Swap the character============
data=(input("Enter the char:"))
d=""
for i in data:
    if ord(i)>=97 and ord(i)<=122:
        d=d+chr((ord(i)-32))
    elif ord(i)>=65 and ord(i)<=90:
         d=d+chr((ord(i)+32)) 
    else:
        d=d+i

print(d)