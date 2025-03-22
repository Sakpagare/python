# to check if a list contains a palindrome of elements

list = [1,2,3,2,1]
list1 = list.copy()
list1.reverse()
if(list == list1):
    print("palindrome")
else:
    print("not palindrome")
