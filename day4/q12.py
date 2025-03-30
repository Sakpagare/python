# read a group if int values from the keyboard as cmd line arguments and print sum
from sys import argv
print("the argument : ",argv)
argv = argv[1:]
sum = 0
for x in argv:
    n = int(x)
    sum = sum + n
print(sum)
