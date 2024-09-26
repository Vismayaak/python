try:
    raise NameError("hi there")
except NameError:
    print("An exception")
    raise