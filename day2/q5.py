# finding the maximum number in list

num_list = [12,3,5,45,33,4]

max  = num_list[0]
for num in num_list :
    if max < num :
        max = num

print(max)
