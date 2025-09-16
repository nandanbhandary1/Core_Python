# C3 Linearization Algorith/Method resolution Order(MRO)\


class A:
    def dispA(self):
        print("Inside A")


a = A()
a.dispA()
print(A.mro())


class B:
    def dispB(self):
        print("Inside B")


b = B()
b.dispB()
print(B.mro())


class C(A, B):
    def dispC(self):
        print("Inside C")


c = C()
c.dispC()
c.dispB()
c.dispA()
print(C.mro())
