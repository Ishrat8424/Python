# Library fine calculator: Accept the number of days a book was kept. There is no fine
# within the 14-day limit, Rs.2 per day for the next 7 days, and Rs.5 per day after that.
# Cap the total fine at the book's price.

days=int(input("enter the no od days:"))
fine=0
if days<=0:
    print("Invalid days....!")
    fine=0

else:
    if days<=14:
        print("No fine....")
    elif days>14 and days<=21:
        fine=(days-14)*2
    elif days>21:
        fine=(7*2)+(days-21)*5

print("=========== Library fine ============ ")
print("Total number of days :",days)
print("total fine:",fine)
print("===================================== ")
print("Thank you....!")