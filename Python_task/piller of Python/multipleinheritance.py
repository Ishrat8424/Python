class A:
    def display(self):
        print("A")

class B:
    def display(self):
        print("B")

class E:
    def display(self):
        print("E")
class F:
    def display(self):
        print("F")

class C(A,B,E,F):
    def disp(self):
        print("C")

C1=C()
C1.disp()
C1.display()