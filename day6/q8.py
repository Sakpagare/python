# list comprehension

nums = [3,4,5,6,7]

sq = []

for num in nums:
    sq.append(num*num)
print(sq)


print([num*num for num in nums])
