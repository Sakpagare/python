# default arguments on mutable datatypes

def add_item(name,employee_data=[]):
    employee_data.append(name)
    print("update data is : ",employee_data)


add_item("jay")
add_item("viru")
add_item("basanti")
add_item("thakur")
