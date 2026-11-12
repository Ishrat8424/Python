class Animal:
    def sleep(self):
        print("\nSleep")

    def eat(self):
        print("Eat")

    def breath(self):
        print("Breath")

class Tiger(Animal):
    def eat(self):
        print("eat both veg and non veg ")

class Monkey(Animal):
    pass
class Dog(Animal):
    pass

T=Tiger()
M=Monkey()
D=Dog()
print("TIGER")
T.sleep()
T.eat()
T.breath()
print("MONKEY")
M.sleep()
M.eat()
M.breath()
print("DOG")
D.sleep()
D.eat()
D.breath()