# find the largest among the three numbers

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

if num1 > num2 and num1 > num3:
    print(f"The {num1} is largest number ")
elif num2 > num3 :
    print(f"The {num2} is largest number ")
else:
    print(f"The {num3} is largest number ")
