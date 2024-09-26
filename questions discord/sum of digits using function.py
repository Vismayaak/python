# def sum_of_digits(n):
#     if n==0:
#         return 0
#     else:
#         return n%10+sum_of_digits(n//10)
# n=int(input("Enter the number:"))
# print(sum_of_digits(n))

# List to hold user data
users = []

def register(username, password):
    # Check if username already exists
    for user in users:
        if user['username'] == username:
            print("Username already exists. Please choose another.")
            return False
            
    # Add new user to the list
    users.append({'username': username, 'password': password})
    print("Registration successful!")
    return True

def login(username, password):
    # Check for the user in the list
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Login successful!")
            return True
    print("Invalid username or password.")
    return False

# Example usage
while True:
    action = input("Do you want to register or login? (r/l): ").lower()
    if action == 'r':
        user = input("Enter username: ")
        pwd = input("Enter password: ")
        register(user, pwd)
    elif action == 'l':
        user = input("Enter username: ")
        pwd = input("Enter password: ")
        login(user, pwd)
    else:
        print("Invalid option, please choose 'r' for register or 'l' for login.")
