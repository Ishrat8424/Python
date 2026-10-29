# Requirements 
# Display ********1234 
# Use slicing only.

aco="987654321234"
print("*"*(len(aco)-4)+aco[-4:])
# for i in range(len(aco)):
#     if i>=len(aco)-4:
#         print(aco[-4:])
#         break
#     else:
#         print("*",end="")