# write a program to display all the leap year present in a user defined range
# Program to display all the leap years in a user-defined range
# def is_leap_year(year):
#     return ((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0))

# sr=int(input("Enter the starting year: "))
# er=int(input("Enter the ending year: "))
# if sr > er:
#     print("Invalid range!")
# else:
#     for i in range(sr, er + 1):
#         if is_leap_year(i):
#             print(i, end=" ")

# display all the leap year and non leap years persent in a user defined range sepatatly
def is_leap_year(year):
    return ((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0))

sr=int(input("Enter the starting year: "))
er=int(input("Enter the ending year: "))
if sr > er:
    print("invalid !")

print("a leap year:")
for i in range(sr, er + 1):
    if is_leap_year(i):
        print(i, end=" ")
        
print("\n not a leap year:")
for i in range(sr,er+1):
    if not is_leap_year(i):
       print(i, end=" ")



