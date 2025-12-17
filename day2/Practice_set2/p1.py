# write a program that asks user for a number and print whether it is possitive ,negative or zero

a = int(input("Enter a Number : "))
print(a)
if a< 0:
    print(a," is Negative ")
elif a == 0:
    print(a," is zero")
else :
    print(a," Positive Number ")