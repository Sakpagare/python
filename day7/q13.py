# mixing variable length keywords and positional arguments

def addition(*num,**nums):
    return(sum(nums.values()))



print(addition(12,2,3,34,n1= 23,n2= 45,n3=78))
