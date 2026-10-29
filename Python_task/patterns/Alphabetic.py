# n=int(input("Enter the number:"))
# alp=96
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(96+j),end=" ")
#     print()
# # a 
# # a b 
# # a b c 
# # a b c d 

# n=int(input("Enter the number:"))
# alp=64
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(chr(64+i),end=" ")

#     print()
# # A A A A 
# # B B B 
# # C C 
# # D 



# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         # print("*",end="")
#         if j%2!=0:
#             print(chr(64+j),end="")

#         else:
#             print(chr(96+j),end="")
        
#     print()

# # AbCd
# # AbCd
# # AbCd
# # AbCd



# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(n,1-1,-1):
#         # print("*",end="")
#         if i%2==0:
#             print(chr(64+j),end=" ")

#         else:
#             print(chr(96+j),end=" ")
        
#     print()
# # d c b a 
# # D C B A 
# # d c b a 
# # D C B A 

# n=int(input("Enter the number:"))
# noc=1
# for i in range(1, n*2):
#     for j in range(1,noc+1):
#         print(chr(96+j),end=" ")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1

# # a 
# # a b 
# # a b c 
# # a b c d 
# # a b c 
# # a b 
# # a 


# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(chr(96+j),end=" ")
#     print()
# # d c b a 
# # d c b 
# # d c 
# # d 


# n=int(input("Enter the number:"))
# noc=n*2-1
# for i in range(1,n+1):
#     for j in range(1,n*2):        
#         if j<=i or j>=noc:
#             print(chr(64+i),end=" ")
            
#         else:
#             print(" ",end=" ")      
#     print()
#     noc-=1
# # A           A 
# # B B       B B 
# # C C C   C C C 
# # D D D D D D D 


# n=int(input("Enter the number:"))
# noc=n
# for i in range(1,n*2):
#     for j in range(1,noc+1):
#         print(chr(96+j),end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1
# # abcd
# # abc
# # ab
# # a
# # ab
# # abc
# # abcd


# n=int(input("Enter the number:"))
# count=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(count+96),end=" ")
#         count+=1
#         if count>26:
#                 count=1
        
#     print()

# # a b c d 
# # e f g h 
# # i j k l 
# # m n o p 
 



# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i+j)%2==0:
#             print(chr(64+j),end=" ")
#         else:
#             print(chr(96+j),end=" ")
#     print()

# # A b C d 
# # a B c D 
# # A b C d 
# # a B c D

# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(i,n+1):
#           print(chr(96+j),end="")
#     print()
# # abcd
# # bcd
# # cd
# # d





# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<j:
#             print(chr(96+i),end="")
#         else:
#             print(chr(96+j),end="")
#     print()

# # aaaa
# # abbb
# # abcc
# # abcd
    

# n= int(input("Enter the number:"))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if i>j:
#             print(chr(96+j),end=" ")
#         else:
#             print(chr(96+i),end=" ")
#     print()

# # d c b a 
# # c c b a 
# # b b b a 
# # a a a a 

# n= int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(i,n+i):
#         print(j,end=" ")
#     print()
# # 1 2 3 4 
# # 2 3 4 5 
# # 3 4 5 6 
# # 4 5 6 7 



# n= int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<j:
#             print(j,end=" ")
#         else:
#             print(i,end=" ")
#     print()
# # 1 2 3 4
# # 2 2 3 4
# # 3 3 3 4
# # 4 4 4 4




# n= int(input("Enter the number:"))
# for i in range(n,1-1,-1):
#     for j in range(1,n+1):
#         if j<i:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#     print()
# # 4 4 4 4 
# # 3 3 3 4 
# # 2 2 3 4 
# # 1 2 3 4 


# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<j:
#             print(chr(96+i),end="")
#         else:
#             print(chr(96+j),end="")
#     print()

# # aaaa
# # abbb
# # abcc
# # abcd


# n=int(input("Enter the number:"))
# for i in range(n,1-1,-1):
#     for j in range(n,1-1,-1):
#         if i>j:
#             print(chr(64+i),end="")
#         else:
#             print(chr(64+j),end="")
#     print()
# # DDDD
# # DCCC
# # DCBB
# # DCBA

# n=int(input("Enter the number:"))
# for i in range(n,1-1,-1):
#     for j in range(n,1-1,-1):
#         if i>j:
#             print(chr(96+j),end=" ")
#         else:
#             print(chr(96+i),end=" ")
#     print()
# # d c b a 
# # c c b a 
# # b b b a 
# # a a a a 


# n=int(input("Enter the number:"))
# for i in range(n,1-1,-1):
#     for j in range(i,1-1,-1):
#         print(chr(96+j),end=" ")
#     print()

# # d c b a 
# # c b a 
# # b a 
# # a 


# n=int(input("Enter the number:"))
# count=1
# intt=64
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(intt+count),end=" ")
#         count+=1
#         if count>26:
#             count=1
#             if intt==64:
#                 intt=96
#             else:
#                 intt=64
#     print()

# # # A B C D E F G H 
# # # I J K L M N O P 
# # # Q R S T U V W X 
# # # Y Z a b c d e f 
# # # g h i j k l m n 
# # # o p q r s t u v 
# # # w x y z A B C D 
# # # E F G H I J K L 



# n=int(input("Enter the number:"))
# noc=1
# nor=n*2-1
# for i in range(1,n*2):
#     for j in range(1,n*2):
#         if j<=noc or j>=nor:
#             print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     if i<n:
#         noc+=1
#         nor-=1
#     else:
#         noc-=1
#         nor+=1
# # 1           1 
# # 2 2       2 2 
# # 3 3 3   3 3 3 
# # 4 4 4 4 4 4 4 
# # 5 5 5   5 5 5 
# # 6 6       6 6 
# # 7           7 




# n=int(input("Enter the number:"))
# nor=n*2-1
# noc=1
# for i in range(n,1-1,-1):
#     for j in range(1,n*2):
#         if noc>=j or j>=nor:
#             print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     noc+=1
#     nor-=1
# # 4           4 
# # 3 3       3 3 
# # 2 2 2   2 2 2 
# # 1 1 1 1 1 1 1



# n=int(input("Enter the number:"))
# nor=n
# noc=n
# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if j<=noc or j>=nor:
#             print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     nor+=1
#     noc-=1
# # 1 1 1 1 1 1 1 
# # 2 2 2   2 2 2 
# # 3 3       3 3 
# # 4           4 



# n=int(input("Enter the number:"))
# noc=n
# for i in range(1,n*2):
#     for k in range(n,noc,-1):
#         print(" ",end=" ")
#     for j in range(noc,1-1,-1):
#         print(j,end=" ")

#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1
# # 4 3 2 1 
# #   3 2 1 
# #     2 1 
# #       1 
# #     2 1 
# #   3 2 1 
# # 4 3 2 1



# n=int(input("Enter the number:"))
# noc=1
# for i in range(1,n*2):
#     for k in range(1,noc):
#         print(" ",end="")
#     for j in range(noc,n+1):
#         print(noc,end=" ")

#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1

# # 1 1 1 1 
# #  2 2 2 
# #   3 3 
# #    4 
# #   3 3 
# #  2 2 2 
# # 1 1 1 1 


# n=int(input("Enter the number:"))
# count=1
# countdec=0
# for i in range(1,n+1):
#     if i%2==0:
#         countdec=countdec+i+1
#     for j in range(i,n+1):
#         if i%2!=0:
#             print(chr(96+count),end="")
#             countdec=count  
#         else:
#             print(chr(96+countdec),end="")
#             countdec-=1
#         count+=1
#     print()
# # Enter the number:4
# # abcd
# # gfe
# # hi
# # n

