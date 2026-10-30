class Demo:
    def __init__(self):
        self.a=10
    @staticmethod
    def eating(x,y=0):
        print(x)
        print(y)
        print("Iam inside the static methord")
        print(a)
        print(b)
        return y+x

d1=Demo()
a=10
b=20
r1=d1.eating(b)
print("sum=",r1)
r2=Demo.eating(10)
print("sum=",r2)
# print(Demo.eating.a)