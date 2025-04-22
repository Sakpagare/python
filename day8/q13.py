# check the given number is odd or even

def fun(num):
    if num % 2 == 0:
        print(f"the {num} is even number ")
    else:
        print(f"the {num} is odd number ")


val = int(input("enter a value : "))
fun(val)
