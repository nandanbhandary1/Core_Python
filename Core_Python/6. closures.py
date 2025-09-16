def outer():
    print("Inside Outer ")

    def inner():
        print("Inside Inner")

    print(inner)
    return inner


ref1 = outer()
print(outer)
print(ref1)
ref1()
