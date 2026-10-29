class Fan:
    def __init__(self):
        self.brand="bajaj"
        self.color="White"
        self.colorr="white"
        self.cost=300
        self.code=300
        print(id(self.cost))
        print(id(self.code))
        print(id(self.color))
        print(id(self.colorr))
        print(self)

Fan()

print(10)