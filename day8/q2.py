# returning function from functions


def value():
    print("Hello ")
    def valuee():
        print("welcome!")

    return valuee


deep = value()

deep()
