# Write a program to check if the given year is a leap year or not
# year = int(input("Enter a year: "))
# if ((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)):
#     print(year, "is a leap year")   
# else:
#     print(year, "is not a leap year")


#Write a program to check if the given year is a leap year or not using customise function
# def is_leap_year(year):
#     if ((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)):
#         return True
#     else:
#         return False

# year = int(input("Enter a year: "))
# if is_leap_year(year):
#     print(year, "is a leap year")  
# else:
#     print(year, "is not a leap year")

#optimised code 
def leapyear(year):
    return ((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0))

year = int(input("Enter a year: "))
if leapyear(year):
    print(year, "is a leap year")
else:   
    print(year, "is not a leap year")
