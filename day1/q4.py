# find the greatest of 3 no. entered by user
num = int(input("enter a no. 1 : "))
num1 = int(input("enter no. 2 : "))
num2 = int(input("enter no. 3 : "))

if(num >= num1 and num >= num2):
    print("num 1 is greater than num2 and num3")
elif(num1 >= num2):
    print("num2 is greater than num1 and num3")
else:
    print("num3 is greater than num2 and num1")

