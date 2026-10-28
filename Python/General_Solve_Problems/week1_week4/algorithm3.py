while True:

    while True:

        month = input("enter month number: ")
        if not month.isnumeric():
            print("must enter numeric")
            continue
        month = int(month)
        if month >12 or month <0:
            print("must between --- [1 - 12] ")
            continue
        else:
            break
    
    if month == 0:
        break


    if month == 1:
        print("January")
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("september")
    elif month == 10:
        print("october")
    elif month == 11:
        print("novomber")
    elif month == 12:
        print("December")