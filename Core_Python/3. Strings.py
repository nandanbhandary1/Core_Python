# s = "Python"
# print(s[2])

# for char in s:
#     print(char, end=" ")


# string = 10
# b = 10

# print(id(string))
# print(id(b))


# string = [1, 2, 3]
# b = [1, 2, 3]
# print(string is b)

# c = 20
# d = 20

# print(string is b)
# print(b is string)
# print(c is string)


# s = "RajaRamMohanRoy"
# print(len(s))
# print(s)
# print(s[0])
# print(s[7])
# print(s[-1])
# print(s[-5])
# print(s[0 : 4])
# print(s[4 : 7])
# print(s[7 : 12])
# print(s[12 : ])
# print(s[ : 7])
# print(s[:])
# print(s[::-1])

# print(s[::3])  # 3 steps Starts from 0

# print(s[:9:-1])

# print(s[6 : 1])

# print(s[-10:-15])

# print(s[-8::-1])

# print(s[-10:-3])

# print(s[4::-1])

# print(s[-2:-12:-1])

# print(s[-13:-6:0])

# print(ord("A"))
# print(ord("@"))
# print(ord("/"))
# print(ord("?"))
# print(ord("+"))


# def lower_to_upper(string):
#     res = ""
#     for char in string:
#         if ord(char) >= 65 and ord(char) <= 90:
#             n = ord(char)
#             res += chr(n + 32)
#         else:
#             res += char
#     return res


# string = input("Enter string name ")

# print(lower_to_upper(string))


# def upper_to_lower(string):
#     res = ""
#     for char in string:
#         if ord(char) >= 97 and ord(char) <= 122:
#             n = ord(char)
#             res += chr(n - 32)
#         else:
#             res += char
#     return res


# string = input("Enter string name ")

# print(upper_to_lower(string))


# def swapcase(string):
#     ans = ""
#     for char in string:
#         if ord(char) >= 65 and ord(char) <= 90:
#             n = ord(char)
#             ans += chr(n + 32)
#         elif ord(char) >= 97 and ord(char) <= 122:
#             n = ord(char)
#             ans += chr(n - 32)
#         else:
#             ans += char
#     return ans


# string = input("Enter string string ")
# print(swapcase(string))


# str1 = "     rana is studyingg      "

# str = str1.lstrip()
# print(str)

# str2 = str1.rstrip()
# print(str2)


# str3 = str1.strip()
# print(str3)


# def remove_space(string):
#     ans = ""
#     for char in string:
#         if char == " ":
#             continue
#         else:
#             ans += char
#     return ans


# string = input("Enter string string ")
# print(remove_space(string))


# def remove_space(string):
#     i = 0
#     ans = ""
#     while i <= len(string) - 1:
#         char = string[i]
#         if char == " ":
#             i += 1
#         else:
#             ans += char
#             i += 1
#     return ans


# string = input("Enter string string ")
# print(remove_space(string))


# GLOBAL DICTIONARY

# str1 = "rama"
# str2 = "sita"
# str3 = "ravana"
# str4 = "rama"
# str5 = "sita"
# str6 = "rama"
# str7 = "ravana"

# print(id(str1))
# print(id(str4))
# print(id(str6))

# print(id(str2))
# print(id(str5))


# str3 = "ravana"
# str7 = "ravana"
# print(id(str3))
# print(id(str7))
# print()

# int1 = 10
# int2 = 10

# print(id(int1))
# print(id(int2))
# print()

# float1 = 10.1
# float2 = 10.1
# print(id(float1))
# print(id(float2))


# str1 = input()
# str2 = input()
# if str1 > str2:
#     print("s1 is big ")
# elif str2 > str1:
#     print("s2 is big")
# else:
#     print("str1 == str2")


# str = "If you think you can, or you can't, you are right"

# str1 = "you"

# print(str.find("you"))
# print(str.index("you"))


# print(str.rfind("you"))
# print(str.rindex("you"))

# print(str.find("python"))
# print(str.index("python"))


# str1 = input()
# if str1.isalpha():
#     print("Only characters")
# elif str1.isdigit():
#     print("Only digit")
# elif str1.isalnum():
#     print("chars or number")


# name = input("Name ")
# age = int(input("age "))
# height = float(input("height "))

# print("Name = {}\nAge = {}\nHeight = {}".format(name, age, height))
# print()
# print("Name = {2}\nAge = {0}\nHeight = {1}".format(age, height, name))
# print(f"Name {name}, Age{age}, Height{height}")


# str1 = "Rama"
# print("Hi {}".format(str1))
# print("Name = {}\n Age = {}\n height = {}\n".format(name, age, height))


# s1 = "Rama is drinking"
# print(s1)

# print(s1.startswith("rama"))
# print(s1.endswith("drinking"))

# s1 = "Rakesh"
# print(s1)
# # s1[5] = "e"
# # print(s1)
# st2 = s1.replace("h", "e")
# print(st2)

# a = 10
# b = 20
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)

# a = 10
# b = 20
# a, b = b, a
# print(a)
# print(b)


# a = 10
# b = 20
# a = a ^ b
# b = b ^ a
# a = a ^ b
# print(a)
# print(b)


# def swap(x, y):
#     temp = x
#     x = y
#     y = temp
#     return x, y


# print(swap(10, 20))


# def disp(x=111, y=222, z=333):
#     print(x)
#     print(y)
#     print(z)


# a = 100
# b = 200
# c = 300
# disp(a, b, c)
# disp(a, b)
# disp(a)
# disp()
# disp(b)
# disp(b, c)
# disp(y=b, z=c)


# def add(x, y):
#     return x + y


# print(add(10, 20))


# def arith(x, y):
#     res1 = x + y
#     res2 = x - y
#     res3 = x * y
#     res4 = x / y
#     return res1, res2, res3, res4


# a1, a2, a3, a4 = arith(10, 20)
# print(a1, a2, a3, a4)


# def topKFrequent(nums, k):
#     count = {}
#     freq = [[] for i in range(len(nums) + 1)]
#     for n in nums:
#         count[n] = count.get(n, 0) + 1
#     for n, c in count.items():
#         freq[c].append(n)
#     res = []
#     for i in range(len(freq) - 1, -1, -1):
#         for n in freq[i]:
#             res.append(n)
#         if len(res) == k:
#             return res


# print(topKFrequent([1, 1, 1, 2, 2, 5, 5, 5, 6, 6, 100], 2))


# class Demo:
#     x = 10

#     def __init__(self):
#         self.y = 20
#         self.z = 30

#     def instance_method(self):
#         print(self.y)
#         print(self.z)

#     @staticmethod  # IF U DONT WRITE THIS AND CALL IT, IT'LL STILL WORK CUZ IT ACTS LIKE A FUNCN
#     def static_method():
#         print(Demo.x)
#         Demo.x = 21
#         print(Demo.x)

#     @classmethod
#     def class_method(cls):
#         print("Python")


# d1 = Demo()
# d1.instance_method()
# Demo.static_method()
# Demo.class_method()


# def sum():
#     a = 10
#     b = 20
#     print(a + b)


# sum()


# class Demo:
#     def __init__(self):
#         self.name = "Python"

#     def disp(self):
#         print(self.name)


# d = Demo()
# d.disp()


# class Demo:
#     x = 10

#     def static_method():  # ACTS AS A FUNCTION NOT AS A STATIC METHOD
#         print(Demo.x)


# Demo.static_method()


# def fun1():
#     print("Hai")


# fun1()


# def fun2():
#     a = 10
#     b = 20
#     print(a + b)


# fun2()


# def fun3(a, b):
#     print(a + b)


# fun3(10, 30)


# def fun4(a, b):
#     return a + b


# print(fun4(40, 55))


# a = 10


# def fun1():
#     print(a)
#     b = 20
#     print(b)


# fun1()


# def fun2():
#     print(a)
#     c = 30
#     print(c)


# print(a)
# fun2()

"""
Change the global var inside a function
"""
# a = 10


# def fun1():
#     global a
#     a = 20
#     print(a)


# print(a)  # U can modify list also by this
# fun1()
# print(a)


# a = 999


# def fun1():
#     a = 888
#     b = 777
#     print(a)
#     print(b)


# def fun2():
#     a = 666
#     c = 555
#     print(a)
#     print(c)


# print(a)
# fun1()
# fun2()
# print(a)


# a = 999

# def fun1():
#     global a
#     a = 888
#     b = 777
#     print(a)
#     print(b)


# def fun2():
#     global a
#     a = 666
#     c = 555
#     print(a)
#     print(c)


# print(a)
# fun1()
# fun2()
# print(a)


# def fun1():
#     print("Hello")


# def fun2(a, b):
#     print(a + b)


# fun1()
# x = 10
# y = 20
# fun2(x, y)

# ptr1 = fun1
# ptr2 = fun2


# print(fun1)
# print(fun2)

# ptr1()
# ptr2(x, y)

# print(ptr1)
# print(ptr2)


# def fun1():
#     print("fun1 invoked")


# def fun2(a, b):
#     c = a + b
#     print("The sum is", c)


# def display(ptr1, ptr2):
#     ptr1()
#     a = 100
#     b = 200
#     ptr2(a, b)


# fun1()
# fun2(10, 20)

# ptr3 = fun1
# ptr4 = fun2

# ptr3()
# x = 20
# y = 30
# ptr4(x, y)
# display(ptr3, ptr4)


# a = lambda x, y: x * y
# print(a(2, 4))


# m = lambda b: b**b
# print(m(9))
