# dictionary comprehension

nums = [1,2,3,4,5,6]

my_dict = {}

for num in nums:
    if num % 2 == 0:
        my_dict[num] = num ** 2

print(my_dict)

print({num:num**2 for num in nums})
