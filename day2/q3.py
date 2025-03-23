#counting the number of occurances of a character in a string
word = "programming"
char = 'g'

count = 0
for i in word :
    if i == char :
        count += 1

print(count)
