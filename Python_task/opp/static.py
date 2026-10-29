# class Farmer:
#     r=2.5
#     def __init__(self,p1,t1):
#         self.p=p1
#         self.t=t1

#     def display(self):
#         s1=(self.p*self.t*Farmer.r)/100
#         print(s1)


# f1=Farmer(200000,2)
# f2=Farmer(500000,5)
# f3=Farmer(1000000,10)

# f1.display()
# f2.display()
# f3.display()


class Demo:
    x=10
    def __init__(self):
        self.y=15
        self.z=5

    def instancedisplay(self):
        print(self.y)
        print(self.z)


    @staticmethod
    def staticdisp():
        print(Demo.x)
        print(self.z)

    @classmethod
    def classdisplay(cls):
        print("Python")
        print(self.z)
        print(Demo.x)


d1=Demo()
d1.instancedisplay()
Demo.staticdisp()
Demo.classdisplay()