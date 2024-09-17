userlogin={}
while True:
    print("Menu")
    print("1.REGISTER")
    print("2.LOGIN")
    print("3.EXIT")
    choice=input("Enter Your Choice")
    if choice=='1':
        print("register")
        username=input("Enter username")
        if username in userlogin:
            print("Username already exists")
        else:
            password=input("Enter password:")
            userlogin[username]=password
            print("Registration successfull")
    elif choice=='2':
        print("Login")
        username=input("Enter your username")
        if username not in userlogin:
            print("username not found")
        else:
            password=input("enter password: ")
            if userlogin[username]==password:
                print("Successfully logged in")
            else:
                print("incorrect password.please try again")
    elif choice=='3':
        print("Exit")
        break
    else:
        print("Invalid choice")