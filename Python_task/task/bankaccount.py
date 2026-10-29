class BankAccount:
    bank_name = "KGS Bank"
    total_accounts = 0 
    amt=1000

    def __init__(self,name,balance):
        self.account_holder=name
        self.Balance=balance
        BankAccount.total_accounts+=1

    @staticmethod
    def deposit(amount):
        BankAccount.amt+=amount

    @staticmethod    
    def withdraw(amount):
        BankAccount.amt-=amount

    def display(self):
        
        print("\nName:",self.account_holder)
        print("Balance:",self.Balance)
        BankAccount.amt+=self.Balance

while True:
    print("\n1.Create the Account\n2.Deposit\n3.Withdraw\n4.Exit")
    choice=int(input("your choice:"))

    if choice==1:
        name=input("\nEnter Name:")
        balance=int(input("Balance:"))
        d1=BankAccount(name,balance)
        d1.display()

    elif choice==2:
        amount=int(input("\nEnter the amount to Withdraw:"))
        BankAccount.deposit(amount)
    elif choice==3:
        amount=int(input("\nEnter the amount to Deposit:"))
        BankAccount.withdraw(amount)
    else:
        print("\nDone with work exiting.......")
        break
print("Total account is:",BankAccount.total_accounts)
print("Total Balance is:",BankAccount.amt)
