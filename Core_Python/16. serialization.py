# import pickle


# class Employee:
#     def __init__(self, name, age, sal, addr):
#         self.ename = name
#         self.eage = age
#         self.esal = sal
#         self.eaddr = addr

#     def disp(self):
#         print(self.ename)
#         print(self.eage)
#         print(self.esal)
#         print(self.eaddr)


# e = Employee("Nandan", 25, 25000, "Kundapura")
# f = open("hello.txt", "wb")
# pickle.dump(e, f)
# print("Object saved to file")
# f.close()


# De-plicking

# f = open("hello.txt", "rb")
# e = pickle.load(f)
# e.disp()
# print("Obj is retrived")
