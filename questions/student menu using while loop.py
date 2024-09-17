students={}
while True:
    print("menu")
    print("1.Registration")
    print("2.Display")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        a=int(input("Enter Number of Students:"))
        for i in range(a):
            dict={}
            id=int(input("Enter your id:"))
            if id in students:
                print("id already exists")
                break
            Name=input("Enter the name:")
            dict["Name"]=Name
            Age=int(input("Enter the age:"))
            dict["Age"]=Age
            Marks=int(input("Enter the marks"))
            dict["Marks"]=Marks
            students[id]=dict
    elif choice==2:
        if students:
            Name=input("Enter name of the person to display: ")
            b={key:value for key,value in students.items() if value["Name"]==Name}
            print(b)
    elif choice==3:
        print("Exit")

    
    
    

        