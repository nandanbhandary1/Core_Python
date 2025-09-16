# a = int(input("Enter the value for a "))
# b = int(input("Enter the value for b "))
# res = a / b
# print("The result is", res)
# print("Program ended ")


# a = int(input("Enter the value for a "))
# b = int(input("Enter the value for b "))
# try:
#     res = a / b
# except Exception as e:
#     print("Error banthooooo")
# # print("Program ended ")

# else:
#     print("Error bandiloooooooo")


# def fun1():
#     print("Enterinf fun1")

#     try:
#         fun2()

#     except Exception as e:
#         print("Error in fun1 ")

#     print("Leaving fun1 ")


# def fun2():
#     print("Entering fun2 ")
#     res = 10 / 0
#     print(res)
#     print("Leaving fun2")


# print("Program Started")
# fun1()
# print("Program Ended")


# def fun1():
#     print("Enterinf fun1")

#     try:
#         fun2()

#     except Exception as e:
#         print("Error in fun1 ")

#     print("Leaving fun1 ")


# def fun2():
#     print("Entering fun2 ")
#     try:

#         res = 10 / 0
#         print(res)
#     except Exception as e:
#         print("Error in fun2 ")
#     print("Leaving fun2")
#     raise e


# print("Program Started")
# fun1()
# print("Program Ended")


"""
HANDLING SPECIFIC EXCEPTION
#"""

# try:
#     a = int(input("Enter the value for a "))
#     b = int(input("Enter the value for b "))
#     res = a / b
# except ValueError as e:
#     print(e.__str__)
#     print("It is VE")

# except ZeroDivisionError as e:
#     print(e.__str__)
#     print("It is a ZDE ")

# except Exception as e:
#     print(e.__str__)
#     print("It is an Error")

# print("Program Ended")


# def fun1():
#     print("Fun 1 connected to DB ")
#     try:
#         fun2()
#     except Exception as e:
#         print("Error in fun1 ")
#         raise e
#     finally:
#         print("Fun1 closing DB ")


# def fun2():
#     print("Fun2 connected to DB")
#     try:
#         res = 10 / 0
#         print(res)
#     except Exception as e:
#         print("Error in fun2 ")
#         raise e
#     finally:
#         print("Fun2 closing DB")


# print("Program Started")
# try:
#     fun1()
# except Exception as e:
#     print("Error in main ")

# print("Program Ended")
