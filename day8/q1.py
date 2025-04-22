#function passing as arguments

def get_name():
    name = input("Enter a name: ")
    sname = input("Enter a surname: ")
    return name + " " + sname

def display(fun):
    print(fun())


display(get_name)
    
