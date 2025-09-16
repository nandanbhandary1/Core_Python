# def print_msg():
#     print("Hello Everyone ")


# def outer(print1):
#     print("Entering outer ")

#     def inner():
#         print("Entering Inner ")
#         ref = print1
#         ref()
#         print("Leaving Inner")

#     return inner


# ptr1 = print_msg
# ptr2 = outer(ptr1)
# ptr2()


def print_msg():
    msg = "Hello everyone"
    return msg


def outer(print1):
    print("Entering outer ")

    def inner():
        print("Entering inner ")
        ref = print1
        msg2 = ref()
        new_var = msg2.upper()
        print(new_var)
        print("Leaving inner")

    return inner()


ptr1 = outer(print_msg)
