# nested function

def outer():
    print("Hello world")
    def inner():
        print("welcome")

    inner()

outer()
