# improve a simple calculator

a = int(input("Enter a : "))
b = int(input("Enter b : "))

ope = input("choose your operation : ")

match ope :
    case "+":
        print("a + b = ",(a+b))
    case "-":
        print("a - b = ",(a-b))
    case "*":
        print("a * b = ",(a*b))
    case "/":
        print("a/b = ",(a/b))

    case _:
        print("oppssssss")