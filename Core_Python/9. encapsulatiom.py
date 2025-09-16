# class Book:
#     def __init__(self, value):
#         self.__pages = value

#     def setter(self, value):
#         if value > 0:
#             self.__pages = value

#     def getter(self):
#         return self.__pages


# b = Book(100)


# # Trying to access private variable directly (will raise AttributeError)
# # print(b.__pages)


# # Accessing private variable through a public method getter
# print(b.getter())

# # Accessing private variable using name mangling (discouraged)
# print(b._Book__pages)


# b.setter(200)
# print(b.getter())


# class Person:
#     def __init__(self):
#         self.name = " "

#     def setter(self, value):
#         self.__name = value

#     def getter(self):
#         return self.__name


# p = Person()
# p.setter("NANDAN")
# print(p.getter())


"""

property function
"""


# class Student:
#     def __init__(self):
#         self.__name1 = " "
#         self.__name2 = " "

#     def setter1(self, value):
#         self.__name1 = value

#     def getter1(self):
#         return self.__name1

#     getset = property(getter1, setter1)

#     def setter2(self, value):
#         self.__name2 = value

#     def getter2(self):
#         return self.__name2

#     setget = property(getter2, setter2)


# s = Student()
# s.getset = "RAMA"

# print(s.getset)

# s.setget = "SITA"
# print(s.setget)


"""  
Property decorator
"""


class Student:
    def __init__(self):
        self.name = " "

    @property
    def dataAccess(self):
        return self.__name

    @dataAccess.setter
    def dataAccess(self, value):
        self.__name = value


s = Student()
s.dataAccess = "Radha"
print(s.dataAccess)

res1 = s.dataAccess
print(res1)
