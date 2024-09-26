# n=int(input("Enter the number:"))
# temp=n
# sum_of_num=0
# length_of_digits=len(str(n))
# while temp>0:
#     digit=temp%10
#     sum_of_num+=digit**length_of_digits
#     temp//=10   
# if sum_of_num==n:
#     print("it is an amstrong number")
# else:
#     print("not an amstrong number")




books = {}
users = {}
admin_credentials = {'admin': 'password'}  # Predefined admin credentials

def add_book( book_id, title, author, quantity):
    books[book_id] = {'title': title,'author': author,'quantity': quantity}
    print(f"Book '{title}' added successfully.")

def update_book(book_id, title=None, author=None, quantity=None):
    if book_id in books:
        if title:
            books[book_id]['title'] = title
        if author:
            books[book_id]['author'] = author
        if quantity is not None:
            books[book_id]['quantity'] = quantity
        print(f"Book ID '{book_id}' updated successfully.")
    else:
        print("Book not found.")

def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        print(f"Book ID '{book_id}' deleted successfully.")
    else:
        print("Book not found.")

def display_all_books():
    if not books:
        print("No books available ")
    else:
        for book_id, details in books.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Quantity: {details['quantity']}")

def register_user(name, age, address, phone_number, username, password):
    if username in users:
        print("Username already exists. Try another.")
    elif phone_number in [user['phone_number'] for user in users.values()]:
        print("Phone number already registered")
    else:
        users[username] = {'name': name,'age': age,'address': address,'phone_number': phone_number,'password': password}
        print(f"User '{name}' registered successfully.")

def login_user(username, password):
    if username in users and users[username]['password'] == password:
        return True
    return False

def search_book_by_name():
    found_books = [book for book in books.values()]
    if found_books:
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
    else:
        print("No books found with that title.")


def main():

    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if username in admin_credentials and admin_credentials[username] == password:
                while True:
                    print("\nAdmin Menu:")
                    print("1. Add Book")
                    print("2. Update Book")
                    print("3. Delete Book")
                    print("4. Display All Books")
                    print("5. Exit")
                    choice = input("Select an option: ")

                    if choice == '1':
                        book_id = input("Enter book ID: ")
                        title = input("Enter book title: ")
                        author = input("Enter book author: ")
                        quantity = int(input("Enter book quantity: "))
                        add_book(book_id, title, author, quantity)

                    elif choice == '2':
                        book_id = input("Enter book ID to update: ")
                        title = input("Enter new title (leave blank to skip): ")
                        author = input("Enter new author (leave blank to skip): ")
                        quantity = input("Enter new quantity (leave blank to skip): ")
                        quantity = int(quantity) if quantity else None
                        update_book(book_id, title or None, author or None, quantity)

                    elif choice == '3':
                        book_id = input("Enter book ID to delete: ")
                        delete_book(book_id)

                    elif choice == '4':
                        display_all_books()

                    elif choice == '5':
                        break

                    else:
                        print("Invalid option.")

            else:
                print("Invalid credentials.")

        elif choice == '2':
            while True:
                print("\nUser Menu:")
                print("1. Registration")
                print("2. Login")
                print("3. Exit")
                choice = input("Select an option: ")

                if choice == '1':
                    name = input("Enter your name: ")
                    age = input("Enter your age: ")
                    address = input("Enter your address: ")
                    phone_number = input("Enter your phone number: ")
                    username = input("Enter a username: ")
                    password = input("Enter a password: ")
                    register_user(name, age, address, phone_number, username, password)

                elif choice == '2':
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    if login_user(username, password):
                        while True:
                            print("\nUser Actions:")
                            print("1. Display All Books")
                            print("2. Search Book by Name")
                            print("3. Exit")
                            choice = input("Select an option: ")

                            if choice == '1':
                                display_all_books()

                            elif choice == '2':
                                title = input("Enter book title to search: ")
                                search_book_by_name()

                            elif choice == '3':
                                break

                            else:
                                print("Invalid option.")
                    else:
                        print("Invalid username or password.")

                elif choice == '3':
                    break

                else:
                    print("Invalid option.")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option.")


    if __name__ == "__main__":
        main()

