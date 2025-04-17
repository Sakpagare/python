# mixing multiple types of arguments
''' 1.positional arguments
    2. variable length positional argument
    3.keyword arguments
    4. variable length keywords arguments
    5 default arguments
    '''

def display(city,*marks,name ="N/A",age=0):
    print(marks)
    print(f"name is :{name}\n age is :{age}\ncity is : {city}")


display("pune",30,40,50,60,name="shantanu",age=23)
