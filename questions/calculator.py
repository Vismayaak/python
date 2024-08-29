print("1.Add \n2.Subtract \n3.multiplication \n4.division\n")
choice1=int(input("enter your choice"))

b=int(input("enter the second number:"))

if(choice1==1):
    print("a+b:",a+b)
elif(choice1==2):
    print("a-b:",a-b)
elif(choice1==3):
    print("a*b:",a*b)
elif(choice1==4):
    print("a/b:",a/b)
else:
    print("invalid choice")
