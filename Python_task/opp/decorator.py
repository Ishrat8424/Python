def outer(fun):
    print("Entering outer 1")
    def inner():
        print("entring inner 2")
        print("processing 3")
        ref=fun
        str=ref()
        print(str.upper())
        print("Leaving inner 5")
    return inner

@outer
def greet():
    str=input("enter:")
    return str

greet()