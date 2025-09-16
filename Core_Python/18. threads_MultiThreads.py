# a = 20
# b = 10
# c = a + b
# d = a - b
# e = a * b
# f = a / b
# print(c)
# print(d)
# print(e)
# print(f)


"""
Single thread
"""

# import time


# class Demo:
#     def printNames(self):
#         names = ["Rama", "Sita", "Krishna"]
#         for name in names:
#             print(name, end=" ")
#             time.sleep(2)

#         print()

#     def printNum(self):
#         for i in range(10):
#             print(i, end=" ")
#             time.sleep(2)
#         print()

#     def add(self):
#         a = 10
#         b = 20
#         c = a + b
#         print("The Sum is", c)
#         time.sleep(2)


# d = Demo()
# d.printNames()
# d.printNum()
# d.add()


# import time


# def task(name):
#     print(f"Task {name} started")
#     time.sleep(2)  # Simulate a time-consuming operation
#     print(f"Task {name} completed")


# # Single-thread execution
# start_time = time.time()

# task(1)
# task(2)
# task(3)

# end_time = time.time()

# print(f"Total time taken: {end_time - start_time:.2f} seconds")


"""  
Multi Thread 
"""
# from threading import Thread
# import time


# class Task1(Thread):
#     def run(self):
#         names = ["Rama", "Sita", "Krishna"]
#         for name in names:
#             print(name, end=" ")
#             time.sleep(2)

#         print()


# class Task2(Thread):
#     def run(self):
#         for i in range(10):
#             print(i, end=" ")
#             time.sleep(2)
#         print()


# class Task3(Thread):
#     def run(self):
#         a = 10
#         b = 20
#         c = a + b
#         print("The Sum is", c)
#         time.sleep(2)


# t1 = Task1()
# t2 = Task2()
# t3 = Task3()

# t1.start()
# t2.start()
# t3.start()


"""  
WAP IN MULTI THREADING TO PRINT ALL THE EVEN NUMBERS AND ODD NUMBERS IN BETWEEN 0 TO 100
"""

# import time
# from threading import *


# class Task1(Thread):
#     def run(self):
#         for i in range(0, 100, 2):
#             print("Even", i)
#             time.sleep(1)


# class Task2(Thread):
#     def run(self):
#         for i in range(1, 100, 2):
#             print("Odd", i)
#             time.sleep(1)


# t1 = Task1()
# t2 = Task2()

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Program completed")


"""  
WAP IN MULTI THREADING TO PRINT ALL THE EVEN NUMBERS AND ODD NUMBERS IN BETWEEN 0 TO 100
"""

# import threading
# import time

# start = time.perf_counter()


# def print_numbers(n, number_type):
#     for i in range(n):
#         if number_type == "odd" and i % 2 == 1:
#             print(f"Odd: {i}")
#         elif number_type == "even" and i % 2 == 0:
#             print(f"Even: {i}")


# odd_thread = threading.Thread(target=print_numbers, args=(100, "odd"))
# even_thread = threading.Thread(target=print_numbers, args=(100, "even"))

# odd_thread.start()
# even_thread.start()

# odd_thread.join()
# even_thread.join()

# end = time.perf_counter()
# print(f"Execution time: {end - start:.6f} seconds")


####################################################################################################################3


# import threading
# import time

# start = time.perf_counter()


# def print_odd_numbers(n):
#     for i in range(n):
#         if i % 2 == 1:  # Only print odd numbers
#             print(f"Odd: {i}")


# def print_even_numbers(n):
#     for i in range(n):
#         if i % 2 == 0:  # Only print even numbers
#             print(f"Even: {i}")


# # Fixed: Added parentheses for args tuple
# odd_thread = threading.Thread(target=print_odd_numbers, args=[100])
# even_thread = threading.Thread(target=print_even_numbers, args=[100])

# odd_thread.start()
# even_thread.start()

# odd_thread.join()
# even_thread.join()

# end = time.perf_counter()
# print(f"Execution time: {end - start:.6f} seconds")


# import threading
# import time


# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         time.sleep(1)


# # Create a thread
# thread = threading.Thread(target=print_numbers)
# # Start the thread
# thread.start()
# # Wait for the thread to complete
# thread.join()
# print("Thread has finished execution.")


# import threading
# import time


# def make_rotis():
#     print("Making rotis...")
#     time.sleep(3)  # Takes 3 seconds
#     print("Rotis ready!")


# def make_paneer():
#     print("Making paneer butter masala...")
#     time.sleep(4)  # Takes 4 seconds
#     print("Paneer ready!")


# def make_ice_cream():
#     print("Making ice cream...")
#     time.sleep(2)  # Takes 2 seconds
#     print("Ice cream ready!")


# # Create threads
# t1 = threading.Thread(target=make_rotis)
# t2 = threading.Thread(target=make_paneer)
# t3 = threading.Thread(target=make_ice_cream)

# # Start all threads at same time
# t1.start()
# t2.start()
# t3.start()

# # Wait for all to finish
# t1.join()
# t2.join()
# t3.join()

# print("All food ready!")


# import threading
# import time


# def do_something(seconds):
#     print(f"Sleeping for {seconds} second(s)...")
#     time.sleep(seconds)
#     return f"Done sleeping for {seconds} second(s)"


# start = time.perf_counter()

# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[2])
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# finish = time.perf_counter()
# print(f"Finished in {round(finish - start, 2)} second(s)")
