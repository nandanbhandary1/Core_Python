# class Parent:
#     def __init__(self):
#         self.a = 10


# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)  # TO ACCESS PARENT CLASSE'S PROPERTY AND VARIABLE
#         self.b = 20


# c1 = Child()
# print(c1.b)
# print(c1.a)


# class A:
#     def __init__(self):
#         self.a = 10


# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.b = 20


# class C(B):
#     def __init__(self):
#         B.__init__(self)
#         self.c = 30


# c1 = C()

# print(c1.c)
# print(c1.b)
# print(c1.a)


# class A:
#     def __init__(self):
#         self.a = 10


# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.b = 20


# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.c = 30


# c1 = C()

# print(c1.c)
# print(c1.b)
# print(c1.a)


# class Cargo:
#     def takeoff(self):
#         print("Plane is take-off ")

#     def fly(self):
#         print("Plane is flying")

#     def land(self):
#         print("Plane is landing ")

#     def carryc(self):
#         print("plane carry cargo")


# class Passenger:
#     def takeoff(self):
#         print("Plane is take-off ")

#     def fly(self):
#         print("Plane is flying")

#     def land(self):
#         print("Plane is landing ")

#     def carryp(self):
#         print("plane carry passenger")


# class Fighter:
#     def takeoff(self):
#         print("Plane is take-off ")

#     def fly(self):
#         print("Plane is flying")

#     def land(self):
#         print("Plane is landing ")

#     def carryw(self):
#         print("plane carry wepons")


# c = Cargo()
# p = Passenger()
# f = Fighter()
# c.takeoff()
# c.fly()
# c.land()
# c.carryc()
# print()
# p.takeoff()
# p.fly()
# p.land()
# p.carryp()
# print()
# f.takeoff()
# f.fly()
# f.land()
# f.carryw()


# class Plane:
#     def takeoff(self):
#         print("Plane is take-off ")

#     def fly(self):
#         print("Plane is flying")

#     def land(self):
#         print("Plane is landing ")


# class Cargo(Plane):
#     def carryc(self):
#         print("Plane carry cargo ")


# class Passenger(Plane):
#     def carryp(self):
#         print("Plane carry passengers ")


# class Fighter(Plane):
#     def carryw(self):
#         print("Plane carry wepons")


# c = Cargo()
# p = Passenger()
# f = Fighter()

# c.takeoff()
# c.fly()
# c.land()
# c.carryc()
# print()
# p.takeoff()
# p.fly()
# p.land()
# p.carryp()
# print()
# f.takeoff()
# f.fly()
# f.land()
# f.carryw()
# print()


# class Animal:
#     def eat(self):
#         print("Animal is eating")

#     def sleep(slef):
#         print("Animal is sleeping")

#     def breathe(self):
#         print("Animal is breathing ")


# class Tiger(Animal):
#     def eat(self):
#         print("Tiger will hunt and eat ")


# class Deer(Animal):
#     def eat(self):
#         print("Tiger will hunt and eat ")


# class Monkey(Animal):
#     def eat(self):
#         print("Tiger will hunt and eat ")


# t = Tiger()
# d = Deer()
# m = Monkey()

# t.eat()
# t.sleep()
# t.breathe()
# print()
# d.eat()
# d.sleep()
# d.breathe()

# print()
# m.eat()
# m.sleep()
# m.breathe()

"""
SINGLE LEVEL INHERITANCE
PARENT -> CHILD
"""


# class A:
#     def dispA(self):
#         print("Inside dispA")


# class B(A):
#     def dispB(self):
#         print("Inside dispB")


# b = B()
# b.dispB()
# b.dispA()


"""
MULTI LEVEL INHERITANCE
PARENT -> CHILD WILL BE PARENT OF -> CHILD
"""


# class A:
#     def dispA(self):
#         print("Inside dispA")


# class B(A):
#     def dispB(self):
#         print("Inside dispB")


# class C(B):
#     def dispC(self):
#         print("Inside dispC")


# c = C()
# c.dispC()
# c.dispB()
# c.dispA()


"""  
MULTIPLE INHERITANCE
"""


# class A:
#     def dispA(self):
#         print("Inside dispA")


# class B:
#     def dispB(self):
#         print("Inside dispB")


# class C(A, B):  # FIRST IT CONSIDERS FIRST PARENT I.E CLASS A THEN IT CHECKS IN CLASS B
#     def dispC(self):
#         print("Inside dispC")


# c = C()
# c.dispC()
# c.dispB()
# c.dispA()


"""  
HIERARCHIAL INHERITANCE
1 PARENT HAS MORE CHILD
"""


# class A:
#     def dispA(self):
#         print("Inside dispA")


# class B(A):
#     def dispB(self):
#         print("Inside dispB")


# class C(A):
#     def dispC(self):
#         print("Inside dispC")


# b1 = B()
# c1 = C()
# c1.dispC()

# c1.dispA()
# b1.dispB()
# b1.dispA()

# c1.dispB()  # ERROR
