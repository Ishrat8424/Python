class Book:
    def __init__(self):
        self.__page=0
    def sedata(self,value):
        if value>0:
            self.__page=value
    def getdata(self):
        return self.__page
b1=Book()
b1.sedata(100)
data=b1.getdata()
print(data)
