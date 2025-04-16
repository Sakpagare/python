# you can return multiple values

def calci(a,b):
    add = a+b
    sub = a - b

    return add,sub


n1,n2 = calci(12,5)

print("the sum is : ",n1)
print("The substraction is : ",n2)


