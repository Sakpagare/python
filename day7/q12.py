# variable length keywords arguments

def addition(**num):
    return sum(num.values())


print(addition(n1 = 30,n2 = 50,n3 = 67))

print(addition(n1 = 45,n2 = 56))
