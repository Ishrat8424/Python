# class Cargoplane:
#     def fly(self):
#         print("Cargoplane is flying")

#     def land(seld):
#         print("Cargoplane is landing")

#     def takeof(self):
#         print("Cargoplane is takeoff")

#     def carry(self):
#         print("Cargoplane carry Cargo")


# class Psngerplane:
#     def fly(self):
#         print("Passengerplane is flying")

#     def land(seld):
#         print("Passengerplane is landing")

#     def takeof(self):
#         print("Passengerplane is takeoff")

#     def carry(self):
#         print("Passengerplane carry pasanger")


# class Fighterplane:
#     def fly(self):
#         print("Fighterplane is flying")

#     def land(seld):
#         print("Fighterplane is landing")

#     def takeof(self):
#         print("Fighterplane is takeoff")

#     def carry(self):
#         print("Fighterplane carry solders")

# c=Cargoplane()
# p=Psngerplane()
# f=Fighterplane()
# c.fly()
# c.land()
# c.takeof()
# c.carry()

# p.fly()
# p.land()
# p.takeof()
# p.carry()

# f.fly()
# f.land()
# f.takeof()
# f.carry()


class Plane:
    def fly(self):
        print("\nplane is flying")

    def land(seld):
        print("plane is landing")

    def takeof(self):
        print("plane is takeoff")

class cargoplane(Plane):
    def carry(self):
        print("Cargoplane carry Cargo")
        Plane.takeof(self)


class passengerplane(Plane):  
    def carry(self):
        print("Passenger carry Passengers")


class fighterplane(Plane):   
    def carry(self):
        print("fighterplane carry Fighters")

c=cargoplane()
f=fighterplane()
p=passengerplane()
c.fly()
c.land()
c.takeof()
c.carry()

p.fly()
p.land()
p.takeof()
p.carry()

f.fly()
f.land()
f.takeof()
f.carry()