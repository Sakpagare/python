# adding two list elements together

list = [1,2,3]
list1 = [2,3,4,5]

rest = []
for i in range(0,len(list)) :
    rest.append(list[i] + list1[i])

print(rest)
