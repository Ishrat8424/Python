# Movie ticket booking: Calculate the ticket price based on seat class (Silver, Gold,
# Platinum) and age group (child, adult, senior). Add a weekend surcharge and allow
# booking multiple tickets in one go.

print("===== MOVIE TICKET BOOKING SYSTEM =====")
silver = 0
gold = 0
platinum = 0
total = 0
weekendCharge = 0
n = int(input("Enter Number of Tickets: "))

if n <= 0:
    print("Invalid Number of Tickets!")
else:
    print("\n1. Weekday")
    print("2. Weekend")
    day = int(input("Choose Day (1-2): "))

    if day!=1 and day!=2:
        print("Invalid Day!")
    else:
        for i in range(1,n+1):
            print("\n===== TICKET", i, "=====")
            print("1. Silver   - Rs.150")
            print("2. Gold     - Rs.250")
            print("3. Platinum - Rs.350")
            choice=int(input("Choose Seat Class: "))

            if choice==1:
                price=150
                silver+=1
            elif choice==2:
                price=250
                gold+=1
            elif choice==3:
                price=350
                platinum+=1
            else:
                print("Invalid Seat Class!")
                continue

            age=int(input("Enter Age: "))
            while age<0:
                print("Invalid Age!")
                age=int(input("Enter Age Again: "))
            if age<12:
                discount=price*50/100
                category="Child"
            elif age>=60:
                discount=price*30/100
                category="Senior"
            else:
                discount=0
                category="Adult"
            price = price-discount
            if day==2:
                price+=50
                weekendCharge+=50
            total+=price
            print("\nAge Category:",category)
            print("Discount: Rs.",discount)
            print("Ticket Price: Rs.",price)
            print("Ticket Booked Successfully!")

        print("\n===== FINAL BOOKING BILL =====")
        print("Silver Tickets:",silver)
        print("Gold Tickets:",gold)
        print("Platinum Tickets:",platinum)
        print("Total Tickets:",silver+gold+platinum)
        print("Weekend Surcharge: Rs.",weekendCharge)
        print("--------------------------------")
        print("Final Amount: Rs.",total)
        print("--------------------------------")
        print("Thank You! Enjoy Your Movie!")
