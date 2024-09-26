try:
    k=5/0
    print(k)
except ZeroDivisionError:
    print("Cant divide by zero")
finally:
    print("this is always executed")