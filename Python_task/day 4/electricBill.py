# Electricity bill: Calculate the bill from units consumed using slabs
# (first 100 units free, next 100 at Rs.1.5, next 100 at Rs.3, above 300 at Rs.5). 
# Add a fixed charge of Rs.50 if the bill is above zero. 

print("===== ELECTRICITY BILL SYSTEM =====")
units=int(input("Enter the units:"))
bill=0
fixedcharge=0
if units<0:
    print("invalid unists")

else: 
    if units<=100:
        bill=0
    elif units<=200:
        bill=(units-100)*1.5
    elif units<=300:
        bill=(units-200)*3+(100*1.5)
    else:
        bill = (100 * 1.5) + (100 * 3) + (units - 300) * 5

if bill>0:
    fixedcharge=50
total=bill+fixedcharge



print("========== ELECTRICITY BILL ==========")
print("\n===== ELECTRICITY BILL =====")
print("Units Consumed:", units)
print("Electricity Charge: Rs.", bill)
print("Fixed Charge: Rs.", fixedcharge)
print("-------------------------------")
print("Total Bill: Rs.", total)
print("===============================")