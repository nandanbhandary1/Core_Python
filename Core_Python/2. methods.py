class Demo:
    def __init__(self):
        self.a = 10
        self.b = 20

    def disp(self):
        x = 100
        y = 200
        print(x + y)


d1 = Demo()
print(d1.a)
print(d1.b)

d1.disp()


class Demo:
    def __init__(self):
        self.a = 10
        self.b = 20

    def disp(self):
        x = 100
        y = 200
        z = x + y
        return z


d1 = Demo()
print(d1.a)
print(d1.b)


print(d1.disp())


class Demo:
    def __init__(self):
        self.a = 10
        self.b = 20

    def disp(self, x, y):
        z = x + y
        return z


x = 100  # Local var?
y = 200
d1 = Demo()
print(d1.a)
print(d1.b)


print(d1.disp(x, y))


class Fan:
    def __init__(self):
        self.brand = "Usha"
        self.color = "Black"
        self.no_of_blades = 3


f1 = Fan()
f2 = f1
print(f1)  # PRINTS THE ADDRESS
print(f2)

print(id(f1))  # PRINTS THE ID
print(id(f2))


print(f1 is f2)


a = 5
print(id(a))


class Demo:
    def __init__(self):
        self.a = 10
        self.b = 20

    def disp(self):
        print(self.a)
        print(self.b)

        self.c = 30
        self.d = 40


df = Demo()
print(df.a)
print(df.b)
df.disp()
df.e = 50
df.f = 60


class Student:
    def __init__(self, sname, usn, add, mob):
        self.name = sname
        self.usn = usn
        self.add = add
        self.mob = mob


s1 = Student("NANDAN", "1MJ21IS066", "kundapura", 9456)
s2 = Student("RAVANA", "1MJ21IS064", "UDUPI", 945556)


print(s1.usn)
print(s2.name)


class Farmer:
    r = 2.5  # Static variable

    def __init__(self, p1, t1):
        self.p = p1
        self.t = t1

    def disp(self):
        s1 = (self.p * self.t * Farmer.r) / 100
        print(s1)


f1 = Farmer(100000, 2)
f1 = Farmer(100000, 3)

f1.disp()
