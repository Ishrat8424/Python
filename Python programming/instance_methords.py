#Method with no parameter and no return value
class Demo:
    def __init__(self):
        self.a=10
        self.b=20
    def dis(self):
        x=100
        y=200
        z=x+y
        print(z)

d1=Demo()
print(d1.a)
print(d1.b)
d1.dis()

#Methoid with no parameter and return value

class Demo:
    def __init__(self):
        self.a=10
        self.b=20
    def dis(self):
        x=100
        y=200
        z=x+y
        return z

d1=Demo()
print(d1.a)
print(d1.b)
r1=d1.dis() #the r1 memory will be stored in STACK
print(r1)

#Methoid with parameter and return no value
class Demo:
    def __init__(self):
        self.a=10
        self.b=20
    def dis(self,x,y):
        z=x+y
        print(z)

d1=Demo()
print(d1.a)
print(d1.b)
r1=d1.dis(d1.a,d1.b)
r1=d1.dis(10,20) #the r1 memory will be stored in STACK


#Methoid with parameter and return value
class Demo:
    def __init__(self):
        self.a=10
        self.b=20
    def dis(self,x,y):
        z=x+y
        return z

d1=Demo()
print(d1.a)
print(d1.b)
r1=d1.dis(80,20) #the r1 memory will be stored in STACK
print(r1)

#Standard way of writing CLASS
class Student():
    def __init__(self,n1,u1,m1,a1):
        self.name=n1
        self.usn=u1
        self.mob=m1
        self.adress=a1

s1=Student("ishrat","4mk23cso43",124578,"bang")
s2=Student("jahan","4mk23cso74",75588,"Manglor")
print(s1)
print(s1.name)