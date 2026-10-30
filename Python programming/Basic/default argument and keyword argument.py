# class Demo:
#     def disp(self,x=11,y=22,z=33):
#         print(x)
#         print(y)
#         print(z)
#         print("----------------------")

# d1=Demo()
# a=10
# b=20
# c=30
# d1.disp(a)
# d1.disp(b,a)
# d1.disp(x=a,z=c)
# d1.disp(z=a,y=c)

#methord returning multiploe value
class Demo:
    def calcu(self,a,b):
        return a+b,a-b,a*b
d1=Demo()
a=10
b=20
r1,r2,r3=d1.calcu(a,b)
print(r1)
print(r2)
print(r3)