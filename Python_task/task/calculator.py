class  Calculator:

    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b

    @staticmethod
    def  multiply(a,b):
        return a*b
    
    @staticmethod
    def   divid(a,b):
        return a//b
c1=Calculator()
while True:
    n1=int(input("\nenter first num:"))
    n2=int(input("Enter second num:"))
    print("\n1.ADDITION\n2.SUB\n3.DIVISION\n4.MULTIPLICATION\n")
    choice=int(input("Enter you choice:"))
    if choice==1:
        r1=c1.add(n1,n2)
        print("Addition:",r1)
    elif choice==2:
        r2=c1.subtract(n1,n2)
        print("Subtraction:",r2)
    elif choice==3:
        r3=c1.divid(n1,n2)
        print("Divisin",r3)
    elif choice==4:
        r4=c1.multiply(n1,n2)
        print("Multiplication:",r4)
    else:
        print("Invalid Choice..")
        break

    
