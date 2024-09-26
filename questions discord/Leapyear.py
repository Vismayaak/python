Year=int(input("Enter a year:"))
if Year % 4==0:
    if Year % 100==0:
        if Year % 400==0:
            print("It is a leap year")
        else:
            print("not a leap year")
    else:
        print("It is a leap year")
else:
    print("not a leap year")
    