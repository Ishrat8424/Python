# str1="RAMA"
# str2="SITA"
# str3="RAMA"
# str4="SITA"
# str5="RAVANA"
# str6="rama"
# str7="sita"
# print(id(str1))
# print(id(str3))
# print(id(str6))
# print(str1 is str3)
# print(str1 is str6)
# print(str2 is str4)

# str="R A M A"
# str1=" "
# for i in str:
#     if i!=" ":
#         str1=str1+i

# print(str1)

# str1="Rama is Sleeping"
# str2=str1.split()
# str3=" "
# print(str2)
# for i in str2:
#     str3=i+" "+str3
# print(str3)

#string formationg
name="Rama"
age=21
place="Banglore"
print("hi {}!".format(name))
print(f"Hi {name}!")

print("name= {}\nage={}\nplace={}".format(name,age,place))