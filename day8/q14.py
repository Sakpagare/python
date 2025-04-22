# to check a leap year

year = int(input("Enter a year: "))

if year % 4 == 0 or year % 400 == 0 and year % 100 == 0 :
    print("the given year is leap year")
else: 
    print("The year is not a leap year")
