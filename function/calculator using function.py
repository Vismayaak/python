def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
def Calculator():
    while True:
        print("Select one operation")
        print("1.Addition")
        print("2Subtraction")
        print("3.Multiplication")
        print("4.division")
        choice=input("Enter your choice ")
        

        if choice=='1':
            num1=int(input("Enter the first number"))
            num2=int(input("Enter the second number"))
            result=add(num1,num2)
        elif choice=='2':
            num1=int(input("Enter the first number"))
            num2=int(input("Enter the second number"))
            result=subtract(num1,num2)
        elif choice=='3':
            num1=int(input("Enter the first number"))
            num2=int(input("Enter the second number"))
            result=multiply(num1,num2)
        elif choice=='4':
            num1=int(input("Enter the first number"))
            num2=int(input("Enter the second number"))
            result=division(num1,num2)   
        elif choice=='5':
            break
        else:
            print("Enter a valid option")
        print(f"The result is{result}")
Calculator()
    

