books={}
admin_details={'admin':'admin123'}
users={}
def main_menu():
    while True:
        print(" Main menu ")
        print("1.Admin")
        print("2.User")
        print("3.Exit")
        choice=input("Choose an option:")

        if choice=='1':
            admin_menu()
        elif choice=='2':
            user_menu()
        elif choice=='3':
            print("exit")
            break
        else:
            print("invalid choice")
    
def admin_menu():
    username=input("Enter admin username:")
    password=input("ENter password:")

    if username in admin_details and admin_details[username] == password:
        while True:
            print("Admin menu")
            print("1.Add book")
            print("2.Update book")
            print("3.Delete book")
            print("4.Display all books")
            print("5.Exit")
            choice=input("choose an option:")

            if choice=='1':
                add_book()
            elif choice=='2':
                update_book()
            elif choice=='3':
                delete_book()
            elif choice=='4':
                display_books()
            elif choice=='5':
                break
            else:
                print("invalid choice")
    else:
        print("invalid admin details")
def add_book():
        book_id=input("Enter book id:")
        title=input("Enter book title:")
        author=input("enter author name:")
        quantity=int(input("Enter quantity:"))
        books[book_id]={'title':title,'author':author,'quantity':quantity}
        print(f"book'{title}' added successfully.")

def update_book():
        book_id=input("Enter book id to update:")
        if book_id in books:
            title=input("Enter new title:")
            author=input("Enter new author:")
            quantity=input("Enter new quantity:")

            if title:
                books[book_id]['title']==title
            if author:
                books[book_id]['author']==author
            if quantity:
                books[book_id]['quantity']==int(quantity)

            print("Book updated successfully")
        else:
            print("book id not found")

def delete_book():
        book_id = input("Enter book id to delete: ")
        if book_id in books:
            del books[book_id]
            print("Book deleted successfully")
        else:
            print("Book id not found")

def display_books():
        if books:
            print("all books")
            for book_id,details in books.items():
                print(f"id:{book_id},Title:{details['title']},Author:{details['author']}.Quantity:{details['quantity']}") 
        else:
            print("No books available")

def user_menu():
        while True:
            print("User menu")
            print("1.Registration")
            print("2.Login") 
            print("3.exit")
            choice=input("choose an option")

            if choice=='1':
                register_user()
            elif choice=='2':
                login_user()
            elif choice=='3':
                break
            else:
                print("invalid choice")

def register_user():
        name=input("Enter your name:")
        age = input("Enter your age: ")
        address = input("Enter your address: ")
        phone_number = input("Enter your phone number (unique): ")

        if phone_number in [user['phone_number'] for user in users.values()]:
            print("Phone number already registered.")
            return
        username = input("Enter a unique username: ")
        if username in users:
            print("Username already taken.")
            return
        password = input("Enter your password: ")
        users[username] = {'name': name,'age': age,'address': address,'phone_number': phone_number,'password': password}
        print("registration successful")

def login_user():
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username]['password'] == password:
            print(f"login, {users[username]['name']}")
            user_menu()
        else:
            print("Invalid username or password.")  


def user_books():
        while True:
            print("User Options")
            print("1. Display All Books")
            print("2. Search Book by Name")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                display_books()
            elif choice == '2':
                search_book_by_name()
            elif choice == '3':
                break
            else:
                print("Invalid choice") 

def display_books():
    if books:
        print("\nAll Books:")
        for book_id, details in books.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Quantity: {details['quantity']}")
    else:
        print("No books available1.")


def search_book_by_name():
        title = input("Enter the book title to search: ")
        found_books = [details for details in books.values() if title.lower() in details['title'].lower()]

        if found_books:
            print("Search Results")
            for book in found_books:
                print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
        else:
            print("No books found") 
main_menu()
