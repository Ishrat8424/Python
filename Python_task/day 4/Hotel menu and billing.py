print("\n\n=================== WELCOME TO IJK RESTURNT ===================")

print("\nHotel menu and billing")
idli=0
dosa=0
biryani=0
cofee=0     
cond=True
while(cond):
    print("\n1. Idli (Rs.30)")
    print("2. Dosa (Rs.50)")
    print("3. Biryani (Rs.180)")
    print("4. Coffee (Rs.20)")
    print("5. Generate the bill. ")
    choice=int(input("\nChoose the option: "))
    if choice==1:
        idli+=1
    elif choice==2:
        dosa+=1
    elif choice==3:
        biryani+=1
    elif choice==4:
        cofee+=1
    elif choice==5:
        break
    else:
        print("Invalid Choice...!")

total=idli*30+dosa*50+biryani*180+cofee*20
realtotal=total
discount=0
if total>=500:
    discount=(total*10)/100
    total=total-discount
gst=total*5/100
finalprice=total+gst


print("\n========== HOTEL BILL ==========")
print("Item\tQuantity\tPrice")
print("--------------------------------")

if idli > 0:
    print("Idli\t", idli, "\tRs.", idli * 30)
if dosa > 0:
    print("Dosa\t", dosa, "\tRs.", dosa * 50)
if biryani > 0:
    print("Biryani\t", biryani, "\tRs.", biryani * 180)
if cofee > 0:
    print("Coffee\t", cofee, "\tRs.", cofee * 20)

print("--------------------------------")
print("Subtotal: Rs.", realtotal)

if discount > 0:
    print("Discount (10%): Rs.", discount)

print("GST (5%): Rs.", gst)
print("--------------------------------")
print("Final Amount: Rs.", finalprice)
print("================================")
print("Thank You! Visit Again!")


