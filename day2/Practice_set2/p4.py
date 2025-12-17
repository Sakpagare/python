# print the corresponding day of the week using mathch case


num = int(input("Enter number between (1-7) : "))

match num:
    case 1 :
        print("It's monday")
    case 2:
        print("It's tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thurday")
    case 5:
        print("Friday")
    case 6:
        print("saturday")
    case 7:
        print("Sunday")
    case _:
        print("Don't know ")
        