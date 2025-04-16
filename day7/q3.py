# need of return statement

def simple_interest(p,n,r):
    si = (p*r*n)/100
    print("simple interest is : ",si)
    return si

p  = 1000
n = 9
r = 9.25

simple_interest(p,n,r)
total = p + si
print(total)
