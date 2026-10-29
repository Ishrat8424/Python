usercode=1234
balance=10000
print("WELCOM TO ATM")
accept=input("Insert the Card : ")
if(accept=="yes"):
    print("card inserted successfully")
    code=int(input("Enter the 4 digit code : "))
    if(code==usercode):
        print("Correct pin")
        print("select the language")
        print("1. ENGLISH")
        print("2. KANNADA")
        print("3. HINDI")
        lang=int(input("Select the Language : "))
        if(lang==1):
                    print("You have selected ENGLISH")
                    print("Select the operation")
                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Balance")
                    print("4. New Pin")
                    operation=int(input("Select the option:"))
        
                    if(operation==1):
                        print("Enter the account type")
                        print("1.current")
                        print("2.savings")
                        # i need to include the the option 
                        amount=int(input("Enter the amount you want to withdraw:"))
                        if(amount <= 0):
                            print("Invalid amount")
        
                        elif(amount % 100 != 0):
                            print("Invalid amount")
                            print("ATM can dispense only ₹100, ₹200, ₹500 and ₹2000 notes.")
                            print("Please enter the amount in multiples of ₹100.")
        
                        elif(amount > balance):
                            print("Insufficient balance")   
                        else:
                            print("Processing......")
                            print("collect cash")
                            collected=input("collect cash (yes/no): ")
                            if(collected=="yes"):
                                print("1.See the remaining balance")
                                print("2.Continue")
                                optt=int(input("Select the option:"))
                            
                                if(optt==1):
                                    print(balance-amount)
                                elif(optt==2):
                                    print("==========================================")
                                    print("                 ATM NETWORK")
                                    print("------------------------------------------")
                                    print("                   DEPOSIT")
                                    print("                  ₹", amount)
                                    print("------------------------------------------")
                                    print("Card           : DEBIT ****4821")
                                    print("Account        : SAVINGS")
                                    print("------------------------------------------")
                                    print("Transaction    : CASH DEPOSIT")
                                    print("Deposited      : ₹", amount)
                                    print("Balance        : ₹", balance + amount)
                                    print("Status         : SUCCESSFUL")
                                    print("------------------------------------------")
                                    print("Terminal       : ATM-0847")
                                    print("Location       : KUNDAPURA")
                                    print("------------------------------------------")
                                    print("          PLEASE COLLECT YOUR CARD")
                                    print("                THANK YOU")
                                    print("==========================================")
                                
                    elif(operation==2):
                        amount=int(input("enter the amount you want to deposit: "))
                        cashinsert=input("Inserted the cash? (yes/no): ")
                        if(cashinsert=="yes"):
                            print("1.See the remaining balance")
                            print("2.Continue")
                            optt=int(input("Select the option:"))
                            if(optt==1):
                                print(balance+amount)
                            elif(optt==2):
                                    print("==========================================")
                                    print("                 ATM NETWORK")
                                    print("------------------------------------------")
                                    print("                   DEPOSIT")
                                    print("                  ₹", amount)
                                    print("------------------------------------------")
                                    print("Card           : DEBIT ****4821")
                                    print("Account        : SAVINGS")
                                    print("------------------------------------------")
                                    print("Transaction    : CASH DEPOSIT")
                                    print("Deposited      : ₹", amount)
                                    print("Balance        : ₹", balance + amount)
                                    print("Status         : SUCCESSFUL")
                                    print("------------------------------------------")
                                    print("Terminal       : ATM-0847")
                                    print("Location       : KUNDAPURA")
                                    print("------------------------------------------")
                                    print("          PLEASE COLLECT YOUR CARD")
                                    print("                THANK YOU")
                                    print("==========================================")
        
                    elif(operation==3):
                            print("your balance is:",balance)
        
                    elif(operation==4):
                            newpin=int(input("Enter the new pin:"))
                            print("pin changed successfully")
        
        # elif(lang==2):
        #     print("You have selected KANNADA")
        #     print("ಕಾರ್ಯಾಚರಣೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ")
        #     print("1. ಹಣ ತೆಗೆಯಿರಿ")
        #     print("2. ಹಣ ಠೇವಣಿ ಮಾಡಿ")
        #     print("3. ಬ್ಯಾಲೆನ್ಸ್ ನೋಡಿ")
        #     print("4. ಹೊಸ ಪಿನ್ ರಚಿಸಿ")

        #     operation = int(input("ಆಯ್ಕೆಯನ್ನು ನಮೂದಿಸಿ: "))

        #     if(operation == 1):
        #         print("ಖಾತೆಯ ಪ್ರಕಾರವನ್ನು ಆಯ್ಕೆಮಾಡಿ")
        #         print("1. ಕರಂಟ್ ಖಾತೆ")
        #         print("2. ಸೇವಿಂಗ್ಸ್ ಖಾತೆ")

        #         account = int(input("ಆಯ್ಕೆಯನ್ನು ನಮೂದಿಸಿ: "))

        #         amount = int(input("ತೆಗೆಯಬೇಕಾದ ಮೊತ್ತವನ್ನು ನಮೂದಿಸಿ: "))

        #         if(amount <= balance):
        #             print("ಪ್ರಕ್ರಿಯೆ ನಡೆಯುತ್ತಿದೆ......")
        #             print("ದಯವಿಟ್ಟು ಹಣವನ್ನು ಪಡೆದುಕೊಳ್ಳಿ")

        #             collected = input("ನೀವು ಹಣವನ್ನು ಪಡೆದುಕೊಂಡಿರಾ? yes/no: ")

        #             if(collected == "yes"):
        #                 print("1. ಉಳಿದ ಬ್ಯಾಲೆನ್ಸ್ ನೋಡಿ")
        #                 print("2. ರಸೀದಿ ನೋಡಿ")

        #                 optt = int(input("ಆಯ್ಕೆಯನ್ನು ನಮೂದಿಸಿ: "))

        #                 if(optt == 1):
        #                     print("ನಿಮ್ಮ ಉಳಿದ ಬ್ಯಾಲೆನ್ಸ್:", balance - amount)

        #                 elif(optt == 2):
        #                     print("==============================")
        #                     print("          ಎಟಿಎಂ ರಸೀದಿ")
        #                     print("==============================")
        #                     print("ವಹಿವಾಟು       : ಹಣ ತೆಗೆಯುವುದು")
        #                     print("ತೆಗೆದ ಮೊತ್ತ     :", amount)
        #                     print("ಉಳಿದ ಬ್ಯಾಲೆನ್ಸ್ :", balance - amount)
        #                     print("ಸ್ಥಿತಿ          : ಯಶಸ್ವಿ")
        #                     print("==============================")
        #                     print("          ಧನ್ಯವಾದಗಳು!")
        #                     print("==============================")
            
        # elif(lang==3):
        #     print("You have selected HINDI")
        #     print("ऑपरेशन चुनें")
        #     print("1. पैसे निकालें")
        #     print("2. पैसे जमा करें")
        #     print("1. पैसे निकालें")
        #     print("3. बैलेंस देखें")
        #     print("4. नया पिन बनाएं")

        #     operation = int(input("विकल्प चुनें: "))

        #     if(operation == 1):
        #         print("खाता प्रकार चुनें")
        #         print("1. चालू खाता")
        #         print("2. बचत खाता")

        #         account = int(input("विकल्प चुनें: "))

        #         amount = int(input("निकालने की राशि दर्ज करें: "))

        #         if(amount <= 0):
        #              print("अमान्य राशि")

        #         elif(amount % 100 != 0):
        #               print("अमान्य राशि")
        #               print("एटीएम केवल ₹100, ₹200, ₹500 और ₹2000 के नोट देता है")
        #               print("कृपया ₹100 के गुणक में राशि दर्ज करें")

        #         elif(amount > balance):
        #             print("अपर्याप्त बैलेंस")

        #         else:
        #             print("प्रक्रिया जारी है......")
        #             print("कृपया नकद प्राप्त करें")

        #             collected = input("क्या आपने नकद प्राप्त किया? yes/no: ")

        #             if(collected == "yes"):

        #                 print("1. शेष बैलेंस देखें")
        #                 print("2. रसीद देखें")

        #                 optt = int(input("विकल्प चुनें: "))

        #                 if(optt == 1):
        #                     print("आपका शेष बैलेंस है:", balance - amount)

        #                 elif(optt == 2):

        #                     print("==========================================")
        #                     print("                 एटीएम नेटवर्क")
        #                     print("------------------------------------------")
        #                     print("                 नकद निकासी")
        #                     print("                 ₹", amount)
        #                     print("------------------------------------------")
        #                     print("कार्ड          : DEBIT ****4821")

        #                     if(account == 1):
        #                         print("खाता           : चालू खाता")

        #                     elif(account == 2):
        #                         print("खाता           : बचत खाता")

        #                     print("------------------------------------------")
        #                     print("लेन-देन        : नकद निकासी")
        #                     print("निकाली गई राशि : ₹", amount)
        #                     print("शेष बैलेंस     : ₹", balance - amount)
        #                     print("स्थिति         : सफल")
        #                     print("------------------------------------------")
        #                     print("टर्मिनल        : ATM-0847")
        #                     print("स्थान          : KUNDAPURA")
        #                     print("------------------------------------------")
        #                     print("       कृपया अपना कार्ड प्राप्त करें")
        #                     print("                धन्यवाद")
        #                     print("==========================================")

        #     elif(operation == 2):

        #         depo = int(input("जमा करने की राशि दर्ज करें: "))

        #         if(depo <= 0):
        #             print("अमान्य राशि")

        #         elif(depo % 100 != 0):
        #             print("अमान्य राशि")
        #             print("कृपया ₹100 के गुणक में राशि दर्ज करें")

        #         else:
        #             cashinsert = input(
        #         "क्या आपने नकद जमा किया? yes/no: "
        #     )

        #             if(cashinsert == "yes"):

        #                 print("नकद सफलतापूर्वक जमा किया गया")

        #                 print("1. नया बैलेंस देखें")
        #                 print("2. रसीद देखें")

        #                 optt = int(input("विकल्प चुनें: "))

        #                 if(optt == 1):
        #                     print(
        #                 "आपका नया बैलेंस है:",
        #                 balance + depo
        #             )

        #                 elif(optt == 2):

        #                     print("==========================================")
        #                     print("                 एटीएम नेटवर्क")
        #                     print("------------------------------------------")
        #                     print("                  नकद जमा")
        #                     print("                  ₹", depo)
        #                     print("------------------------------------------")
        #                     print("कार्ड          : DEBIT ****4821")
        #                     print("खाता           : बचत खाता")
        #                     print("------------------------------------------")
        #                     print("लेन-देन        : नकद जमा")
        #                     print("जमा राशि       : ₹", depo)
        #                     print("नया बैलेंस     : ₹", balance + depo)
        #                     print("स्थिति         : सफल")
        #                     print("------------------------------------------")
        #                     print("टर्मिनल        : ATM-0847")
        #                     print("स्थान          : KUNDAPURA")
        #                     print("------------------------------------------")
        #                     print("       कृपया अपना कार्ड प्राप्त करें")
        #                     print("                धन्यवाद")
        #                     print("==========================================")

        #     elif(operation == 3):
        #         print("आपका बैलेंस है:", balance)  

        #     elif(operation == 4):
        #         newpin = int(input("नया पिन दर्ज करें: "))
        #         print("पिन सफलतापूर्वक बदल दिया गया")  
                  

        
           
    else:
        print("wrong pin re-enter the code")

else:
    print("Please insert the card")