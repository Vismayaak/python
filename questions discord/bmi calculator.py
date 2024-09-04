height=float(input("enter your height: "))
weight=float(input("enter your weight: "))
bmi=weight/(height**2)
if bmi<18.5:
    print("under weight")
elif bmi>=18.5 and bmi<24.9:
    print("normal weight")
elif bmi>=25 and bmi<29.9:
    print("over weight")
elif bmi>=30:
    print("obese")