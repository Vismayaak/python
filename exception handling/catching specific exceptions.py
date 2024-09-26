def fun(a):
    if a<4:b=a/(a-3)
    print("value of b=",b)
    try:
        fun(3)
    except ZeroDivisionError:
        print("zerodivision error occured")
    except NameError:
        print("Name error occured")