# def sum_list(lst):
#     total=0
#     for n in lst:
#         total=total+n
#     return total
# lst=[1,2,3,4,5]
# print(sum_list(lst))



# Global variables
rooms = []
reservations = []
guests = []
admin_credentials = {"admin": "admin123"}
receptionist_credentials = {"receptionist": "reception123"}
current_guest_id = 1

def main_menu():
    while True:
        print("\n--- Hotel Reservation System ---")
        print("1. Admin")
        print("2. Receptionist")
        print("3. Guest")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            admin_section()
        elif choice == '2':
            receptionist_section()
        elif choice == '3':
            guest_section()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def admin_section():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if admin_credentials.get(username) == password:
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add Room")
            print("2. Update Room Details")
            print("3. Remove Room")
            print("4. View All Reservations")
            print("5. Generate Reports")
            print("6. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                add_room()
            elif choice == '2':
                update_room()
            elif choice == '3':
                remove_room()
            elif choice == '4':
                view_reservations()
            elif choice == '5':
                generate_reports()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid credentials.")

def receptionist_section():
    username = input("Enter receptionist username: ")
    password = input("Enter receptionist password: ")

    if receptionist_credentials.get(username) == password:
        while True:
            print("\n--- Receptionist Menu ---")
            print("1. Check-In Guest")
            print("2. Check-Out Guest")
            print("3. Make Reservation")
            print("4. Cancel Reservation")
            print("5. View Available Rooms")
            print("6. View Guest Details")
            print("7. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                check_in_guest()
            elif choice == '2':
                check_out_guest()
            elif choice == '3':
                make_reservation()
            elif choice == '4':
                cancel_reservation()
            elif choice == '5':
                view_available_rooms()
            elif choice == '6':
                view_guest_details()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid credentials.")

def guest_section():
    global current_guest_id
    while True:
        print("\n--- Guest Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            register_guest()
            current_guest_id += 1
        elif choice == '2':
            login_guest()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def add_room():
    room_number = input("Enter room number: ")
    room_type = input("Enter room type (single/double/suite): ")
    price = float(input("Enter price per night: "))
    availability = input("Is the room available? (yes/no): ").lower() == 'yes'
    rooms.append({
        'room_number': room_number,
        'room_type': room_type,
        'price': price,
        'availability': availability
    })
    print("Room added successfully.")

def update_room():
    room_number = input("Enter room number to update: ")
    for room in rooms:
        if room['room_number'] == room_number:
            room['price'] = float(input("Enter new price per night: "))
            room['availability'] = input("Is the room available? (yes/no): ").lower() == 'yes'
            print("Room details updated successfully.")
            return
    print("Room not found.")

def remove_room():
    room_number = input("Enter room number to remove: ")
    for room in rooms:
        if room['room_number'] == room_number:
            rooms.remove(room)
            print("Room removed successfully.")
            return
    print("Room not found.")

def view_reservations():
    if reservations:
        for reservation in reservations:
            print(reservation)
    else:
        print("No reservations found.")

def generate_reports():
    total_rooms = len(rooms)
    available_rooms = sum(1 for room in rooms if room['availability'])
    occupancy_rate = (total_rooms - available_rooms) / total_rooms * 100 if total_rooms else 0
    print(f"Occupancy Rate: {occupancy_rate:.2f}%")
    print(f"Total Rooms: {total_rooms}, Available Rooms: {available_rooms}")

def check_in_guest():
    guest_id = input("Enter guest ID: ")
    room_number = input("Enter room number: ")
    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")

    for room in rooms:
        if room['room_number'] == room_number and room['availability']:
            room['availability'] = False
            reservations.append({
                'guest_id': guest_id,
                'room_number': room_number,
                'check_in_date': check_in_date,
                'status': 'occupied'
            })
            print("Guest checked in successfully.")
            return
    print("Room not available or not found.")

def check_out_guest():
    guest_id = input("Enter guest ID: ")
    room_number = input("Enter room number: ")

    for reservation in reservations:
        if reservation['guest_id'] == guest_id and reservation['room_number'] == room_number:
            reservation['status'] = 'checked out'
            for room in rooms:
                if room['room_number'] == room_number:
                    room['availability'] = True
                    break
            print("Guest checked out successfully.")
            return
    print("Reservation not found.")

def make_reservation():
    guest_id = input("Enter guest ID: ")
    room_number = input("Enter room number: ")
    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

    for room in rooms:
        if room['room_number'] == room_number and room['availability']:
            room['availability'] = False
            reservations.append({
                'guest_id': guest_id,
                'room_number': room_number,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'status': 'reserved'
            })
            print("Reservation made successfully.")
            return
    print("Room not available or not found.")

def cancel_reservation():
    guest_id = input("Enter guest ID: ")
    for reservation in reservations:
        if reservation['guest_id'] == guest_id:
            reservations.remove(reservation)
            for room in rooms:
                if room['room_number'] == reservation['room_number']:
                    room['availability'] = True
                    break
            print("Reservation canceled successfully.")
            return
    print("Reservation not found.")

def view_available_rooms():  
    available_rooms = [room for room in rooms if room['availability']]
    if available_rooms:
        for room in available_rooms:
            print(room)
    else:
        print("No available rooms.")

def view_guest_details():
    for guest in guests:
        print(guest)

def register_guest():
    global current_guest_id
    name = input("Enter name: ")
    contact = input("Enter contact details: ")
    address = input("Enter address: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    guest = {
        'guest_id': current_guest_id,
        'name': name,
        'contact': contact,
        'address': address,
        'username': username,
        'password': password
    }
    guests.append(guest)
    print("Guest registered successfully.")

def login_guest():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for guest in guests:
        if guest['username'] == username and guest['password'] == password:
            guest_menu(guest['guest_id'])
            return
    print("Invalid credentials.")

def guest_menu(guest_id):
    while True:
        print("\n--- Guest Actions ---")
        print("1. View Available Rooms")
        print("2. Make a Reservation")
        print("3. View Reservation Status")
        print("4. Update Personal Information")
        print("5. Cancel Reservation")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            view_available_rooms()
        elif choice == '2':
            make_reservation()
        elif choice == '3':
            view_reservation_status(guest_id)
        elif choice == '4':
            update_personal_info(guest_id)
        elif choice == '5':
            cancel_reservation()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def view_reservation_status(guest_id):
    reservations_for_guest = [res for res in reservations if res['guest_id'] == guest_id]
    if reservations_for_guest:
        for res in reservations_for_guest:
                    print(res)
    else:
        print("No reservations found.")

def update_personal_info(guest_id):
    for guest in guests:
        if guest['guest_id'] == guest_id:
            guest['contact'] = input("Enter new contact details: ")
            guest['address'] = input("Enter new address: ")
            print("Personal information updated successfully.")
            return
    print("Guest not found.")
main_menu()
 

