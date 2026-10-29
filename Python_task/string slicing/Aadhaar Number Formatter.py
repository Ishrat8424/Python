# Requirements 
# • Print the first 4 digits.  
# • Print the last 4 digits.  
# • Print the middle 4 digits.  
# • Display: 1234-5678-9012 

# num=int("Enter the addhar numbet:")
num="123456781434"
print("Print the first 4 digits:",num[:4])
print(num[-4:])
n=(len(num))
n=n//2
print(num[n-2:n+2])
print(num[:4]+"-"+num[4:8]+"-"+num[8:])
# for i in range(len(num)):
#     print(num[i],end="")
#     if i==3 or i==7:
#         print("-",end="")

