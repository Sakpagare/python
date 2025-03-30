# if there is any way to print all the element by skipping only middle element from array

from sys import argv
print("the argument : ",len(argv))
print("the actual argument : ",argv)
print("command line argument one by one : ")
for x in argv:
    print(x)
print("slice operator : ",argv[1:3])

