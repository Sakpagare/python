# shallow copy and deep copy
import copy
mylist =[[1,2,3],[4,5,6]]

print("id of mylist: ",id(mylist))
print("id of first element: ",id(mylist[0]))
print("id of second element: ",id(mylist[1]))


newlist = copy.copy(mylist)

print("id of newlist : ",id(newlist))
print("id of first element : ",id(newlist[0]))
print("id of second element : ",id(newlist[1]))


newlist[1][2] = 50000
print(mylist)


print(newlist)
