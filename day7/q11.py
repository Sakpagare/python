# variable length line argument


def addition(*num):
    sum = 0
    for i in num:
        sum = sum + i

    return sum


print(addition(10,20,30))
print(addition(10,30))

