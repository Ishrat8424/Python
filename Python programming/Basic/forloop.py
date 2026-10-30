# print(range(1,10,+2))
# print(range(77,80))
# # print(range())
# print(list(range(1,10,+2)))
# Write a program to display the natural numbers from beginning with a difference of three up to n where n is also included
n=8
# for i in range(1, n + 1, 3):
#     print(i,end=" ") 

# Display the natural number starting from n to 1 in the decremention order eith a difference of 4
# for i in range(n, 0, -4):
#     print(i,end=" ")

# when start > end and its increment
# for i in range(n, 0, 4):
#     print(i,end=" ")

#for without range
arr=[1,2,3,4,5,[10,20],["abc","xyz"]]
for i in arr:
    print(i,end=" ")
print("\n================================")
for k in 10,20,30,40,50:
    print(k,end=" ")
print("\n================================")
for i in "1000":
    print(i,end=" ")
print("\n================================")
for j in []:
    print(j,end=" ")
    print("\n================================")
for j in True,False:
    print(j,end=" ")
print("\n================================")
for k in None,True,False:
    print(k,end=" ")