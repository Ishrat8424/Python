def calculate_bill(units):
    def calculate_units():
        bill=units*5
        return bill
    bill=calculate_units()
    return bill

unit=int(input("Enter the input:"))
print("Total bill =",calculate_bill(unit))