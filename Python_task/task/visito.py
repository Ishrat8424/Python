class Visitor:
    def __init__(self):
        self.count=0
        self.visito_Name=""
        self.visito_Time=""

    def check_In(self):
        if self.count==0:
            self.count+=1
            print("\n=================Visitor Check_In =================")
            self.visito_Id=input("Enter Visitor ID : ")
            self.visito_Name=input("Enter Visitor Name : ")
            self.visito_Complay=input("Enter Companay Name : ")
            self.visito_Num=input("Enter Mobile Number : ")          
            self.visito_Meet=input("Person to Meet : ")
            self.visito_Dept=input("Department : ")
            self.visito_Purpose=input("Perpose of visit : ")
            self.visito_Time=int(input("Entry Time (Hour 0-23) : "))
            print("Visitor Checked In Successfully")
            print("Welcome,",self.visito_Name)
            return self.visito_Time
        else :
            print("You have already cheacked In...")
    def check_out(self):
        if self.count==1:
            print("\n=================Visitor Check_Out =================")
            self.exit=int(input("Enter the exit time :"))
            if self.exit<self.visito_Time:
                print("exit time must be more then cheak in time...!")

            else:
                print("exit Time:",abs(self.exit-self.visito_Time))

                print("\n================= Visitor Summary =================")
                print("Visitor ID       :", self.visito_Id)
                print("Visitor Name     :", self.visito_Name)
                print("Company          :", self.visito_Complay)
                print("Mobile           :", self.visito_Num)
                print("Person to Meet   :", self.visito_Meet)
                print("Department       :", self.visito_Dept)
                print("Purpose          :", self.visito_Purpose)
                print("Entry Time       :", self.visito_Time)
                print("Exit Time        :", self.exit)
                print("Visit Duration   :", abs(self.exit-self.visito_Time), "Hours")
                self.count=0
        else:
            print("First Check_In..............!")     

    def guidline(self):
        print("\n========== Visitor Guidelines ==========")
        print("1. Wear your Visitor ID Card.")
        print("2. Photography is not allowed.")
        print("3. Follow company security rules.")
        print("4. Smoking is prohibited.")
        print("5. Return Visitor Pass before leaving.")
        print("6. Report to Reception while exiting.")


start=True  
check_in=Visitor() 
while(start):
    print("\n==========================================")
    print("KAIZENTRIX GLOBAL SOLUTIONS")
    print("Corparate Visitor Management System")
    print("==========================================")
    print("1. Visitor Chick_In")
    print("3. Visitor Chick_Out")
    print("3. Visitor Guidline")
    print("4. Exit")
    choice=int(input("Enter your Choice : "))
    
    if choice==1:
       check_in.check_In()
    elif choice==2:
        check_in.check_out()
    elif choice==3:
        check_in.guidline()
    elif choice==4:
        start=False
    else:
        print("Choose the correct option...!")  