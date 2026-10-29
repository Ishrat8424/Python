# class Fan:
#     def __init__(self):
#         self.brand="bajaj"
#         self.color="black" 
#         self.cost=3000
#         self.noOfBlades=3

#     def on(self):
#             print("fan is on")

#     def rotate(self):
#             print("fan is rotating")

# f1=Fan()
# print(f1.brand)
# print(f1.color)
# print(f1.cost)
# print(f1.noOfBlades)

# f1.on( )
# f1.rotate( )

class Student:
    def __init__(self):
        self.name="Ishrat"
        self.usn="4MK23CS043"
        self.address="Banglore"
        self.quali="B.E"

    def eat(self,dog):
        print(dog)
        print("student eat")
        print(self.name)

    def study(self):
        print("student study")

s1=Student()
print(s1.name)
print(s1.usn)
print(s1.address)
print(s1.quali)

# s1.eat()
s1.study()

print("after modufying the properties")
s1.mob=12345
print(s1.mob)
s2=s1
# s2.eat()

s1.name="Rashmi"
print(s1.name)  

a=10
print(type(a))

s1.eat(dog="Dogg")