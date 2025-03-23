# counting vowels in a given words
vowel = ['a','e','i','o','u']
word = "programming"

count = 0
for char in word : 
    if char in vowel :
        count +=1

print(count)
