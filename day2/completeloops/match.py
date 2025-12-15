n = int(input("choose a number between 1 to 10 : "))

match n :
    case 1:
        print("YOu get 500$")
    case 5:
        print("you get teddy")
    case 9:
        print("you get bike")
    case _:
        print("better luck next time!!!!!")