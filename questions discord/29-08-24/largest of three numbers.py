num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
largest=num1
if(num1>num2):
    if(num1>num3):
        largest=num1
    else:
        largest=num3
else:
    if(num2>num3):
        largest=num2
    else:
        largest=num3
print(f"the largest number is {largest}")