admin_details={"admin":"admin123"}

def main_menu():
    print("Main menu:")
    print("1.Admin")
    print("2.User")
    print("3.Exit")
    choice=input("Select an option")
    if choice=='1':
        admin_section()
    elif choice=='3':
        user_section()
    elif choice=='3':
        print("exit")
    else:
        print("invalid choice")

def admin_section():
    username=input("Enter admin username:")
    password=input("Enter admin password:")
    if admin_details.get(username)==password:
        while True:
            print("Admin menu")
            print("1.Add product")
            print("2.update product")
            print("3.remove product")
            print("4.view all products")
            print("5.view orders")
            print("6.exit")

            choice=input("enter an option:")
            if choice=='1':
                add_product()
            elif choice=='2':
                update_product()
            elif choice=='3':
                remove_product()
            elif choice=='4':
                view_product()
            elif choice=='5':
                view_order()
            elif choice=='6':
                print("exit")
                break
            else:
                print("invalid choice")
    else:
        print("invalid username or password")

def user_section():
    while True:
        print("User menu:")
        print("1.register")
        print("2.login")
        print("3.exit")

        choice=input("select an option:")
        if choice=='1':
            register()
        elif choice=='2':
            