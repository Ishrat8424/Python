# class Person:
#     def __init__(self):
#         self.__name=""

#     def setdata(self,value):
#         self.__name=value

#     def getdata(self):
#         return self.__name
#     getset=property(getdata,setdata)

# p1=Person()
# p1.getset="Rama"
# res=p1.getset
# print(res)



class Person:
    def __init__(self): 
        self.__name=""

    @property
    def dataaccess(self):
        return self.__name
    
    @dataaccess.setter
    def dataaccess(self,value):
        self.__name=value


p1=Person()
p1.dataaccess="Rama"
res=p1.dataaccess
print(res)