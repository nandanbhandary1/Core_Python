# l = []
# i = 0
# while i <= 4:
#     print("Enter the number ")
#     data = int(input())
#     l.insert(i, data)
#     i += 1
# print(l)

# print()

# for num in l:
#     print(num)


# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# l = []
# i = 0
# while i <= 4:
#     print("Enter the value ")
#     data = int(input())
#     l.insert(i, data)
#     i += 1
# print(l)

# i = 0
# while i <= 4:
#     ext = l[i]
#     status = even(ext)
#     if status:
#         print(l[i])
#     i += 1


# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# l = []
# i = 0
# while i <= 4:
#     data = int(input())
#     l.insert(i, data)
#     i = i + 1
# print(l)

# k = list(filter(even, l))
# print(k)


# l = []
# i = 0
# while i <= 4:
#     data = int(input())
#     l.insert(i, data)
#     i = i + 1
# print(l)

# k = list(filter(lambda num: (num % 2 == 0), l))
# print(k)


# def operation(data):
#     return data + 10


# l = [10, 20, 30, 40, 50]
# k = list(map(operation, l))
# print(k)

# l = [10, 20, 30, 40, 50]

# k = list(map(lambda num: (num + 10), l))
# print(k)

# l = ["Rama", "Sita", "Ravana", "Krishna", "Ramesh"]

# k = list(filter(lambda name: (name.startswith("R")), l))
# print(k)

# l = ["Rama", "Sita", "Ravana", "Krishna", "Ramesh"]

# k = list(map(lambda name: (name.upper()), l))

# print(l)
# print(k)


# def outer():
#     print("Inside outer ")

#     def inner():
#         print("Inside Inner")

#     inner()


# outer()


# def outer():
#     print("Inside outer ")

#     def inner():
#         print("Inside Inner")

#     inner()


# outer()


# def fun1():
#     a = 10  # Non local variable for fun2() but local variable for fun1()
#     print(a)

#     def fun2():
#         nonlocal a
#         a = 20  # Non local variable for fun3() but local variable for fun2()
#         print(a)

#         def fun3():
#             c = 30  # local variable for fun3()
#             print(c)

#         fun3()

#     fun2()

#     print(a)


# fun1()


# fun1()
# def fun1():
#     a = 10  # NON - LOCAL VARIABLE
#     print(a)

#     def fun2():
#         b = 20  # LOCAL VARIABLE
#         print(b)

#     fun2()


# fun1()


# def fun1():
#     a = 10  # ✅ Local variable for fun1()
#     # 🔁 Enclosing variable for fun2(), but NOT nonlocal unless declared as such
#     print(a)

#     def fun2():
#         b = 20  # ✅ Local variable for fun2()
#         # 🔁 Enclosing variable for fun3(), not nonlocal unless declared as such
#         print(b)

#         def fun3():
#             c = 30  # ✅ Local variable for fun3()
#             print(c)

#         fun3()

#     fun2()


# fun1()


# def fun1():
#     a = 10
#     print(a)

#     def fun2():
#         nonlocal a
#         a = 20
#         b = 30
#         print(a)
#         print(b)

#     fun2()
#     print(a)


# fun1()


from math import pi

# pi = 10


def fun1():
    # pi = 15

    def fun2():
        # pi = 20
        print(pi)

    fun2()


fun1()
