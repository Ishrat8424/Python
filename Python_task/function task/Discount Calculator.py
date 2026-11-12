def discount_generator(discount):
    def calculate(price):
        finalprice=price-(price*discount/100)
        return finalprice
    return calculate

amount=int(input("Enter the amount:"))
discount=int(input("Enter the discount:"))
cal=discount_generator(discount)
print("Thee final amount is ",cal(amount))
