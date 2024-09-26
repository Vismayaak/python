rooms=[]
reservations=[]
guests=[]
admin_details={"admin":"admin123"}
receptionist_details={"receptionist":"receptionist123"}
guest_id=1
def main_menu():
    while True:
        print("Hotel Reservation")
        print("1.Admin")
        print("2.recepetion")
        print("3.guest")
        print("4.exit")
        choice=input("Select an option:")

        if choice=='1':
            admin_section()
        elif choice=='2':
            reception_section()
        elif choice=='3':
            guest_section()
        elif choice=='4':
            print("exit")
            break
        else:
            print("invalid choice")

def admin_section():
    username=input("Enter admin username:")
    password=input("Enter the password:")
    if admin_details.get(username)==password:
        while True:
            print("Admin menu")
            print("1.add room")
            print("2.update room details")
            print("3.remove room")
            print("4.view all reservations")
            print("5.generate reports")
            print("6.exit")
            choice=input("select an option:")
            if choice=='1':
                add_room()
            elif choice=='2':
                update_room()
            elif choice=='3':
                remove_room()
            elif choice=='4':
                view_reservations()
            elif choice=='5':
                generate_reports()
            elif choice=='6':
                break
            else:
                print("invalid choice")
    else:
        print("invalid")

def reception_section():
    username=input("Enter username:")
    password=input("Enter password:")
    if receptionist_details.get(username)==password:
        while True:
            print("reception menu")
            print("1.check in")
            print("2.checkout")
            print("3.make reservation")
            print("4.cancel reservation")
            print("5.view available rooms")
            print("6.view guest details")
            print("7.exit")
            choice=input("select an option:")
            if choice=='1':
                check_in()
            elif choice=='2':
                check_out()
            elif choice=='3':
                make_reservation()
            elif choice=='4':
                cancel_reservation()
            elif choice=='5':
                view_available_rooms()
            elif choice=='6':
                view_guest_details()
            elif choice=='7':
                break
            else:
                print("invalid choice")
    else:
        print("invalid")

def guest_section():
    global guest_id
    while True:
        print("guest menu")
        print("1.register")
        print("2.login")
        print("3.exit")
        choice=input("select an option")
        if choice=='1':
            register_guest()
            guest_id+=1
        elif choice=='2':
            login_guest()
        elif choice=='3':
            break
        else:
            print("invalid choice")

def add_room():
    room_number = input("Enter room number: ")
    for room in rooms:
        if room['room_number'] == room_number:
            print("Room already exists.")
            return
    room_type = input("Enter room type (single or double or suite): ")
    price = float(input("Enter price: "))
    availability = input("room available or not? (yes/no): ").lower()=='yes'
    rooms.append({'room_number': room_number,'room_type': room_type,'price': price,'availability': availability})
    print("Room added successfully.")

def update_room():
    room_number = input("Enter room number to update: ")
    for i in rooms:
        if i['room_number'] == room_number:
            i['price'] = float(input("Enter new price per night: "))
            i['availability'] = input("Is the room available? (yes/no): ").lower()=='yes'
            print("Room details updated successfully.")
            return
    print("Room not found.")

def remove_room():
    room_number = input("Enter room number to remove: ")
    for i in rooms:
        if i['room_number'] == room_number:
            rooms.remove(i)
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

def check_in():
    guest_id = input("Enter guest ID: ")
    room_number = input("Enter room number: ")
    check_in_date = input("Enter check-in date: ")
    for room in rooms:
        if room['room_number'] == room_number and room['availability']:
            room['availability'] = False
            reservations.append({'guest_id': guest_id,'room_number': room_number,'check_in_date': check_in_date,'status': 'occupied'})
            print("Guest checked in successfully.")
            return
    print("Room not available or not found.")

def check_out():
    guest_id=input("Enter guest ID:")
    room_number=input("Enter room number:")
    for res in reservations:
        if res['guest_id']==guest_id and res['room_number']==room_number:
            res['status']='checked out'
            for i in rooms:
                if i['room_number']==room_number:
                    i['availability']=True
                    break
            print("Guest checked out successfully")
            return
    print("reservation not found")
    
def make_reservation():
    guest_id=input("Enter guest id:")
    room_number=input("enter room number:")
    check_in_date=input("Enter check in date:")
    check_out_date=input("Enter check out date:")
    for r in rooms:
        if r['room_number']==room_number and r['availability']:
            r['availability']=False
            reservations.append({'guest_id':guest_id,'room_number':room_number,'check_in_date':check_in_date,'check_out_date':check_out_date,'status':'reserved'})
            print("Reservation made successfully")
            return
    print("Room not available.")

def cancel_reservation():
    guest_id=input("Enter guest id:")
    for reservation in reservations:
        if reservation['guest_id']==guest_id:
            reservations.remove(reservation)
            for room in rooms:
                if room['room_number']==reservation['room_number']:
                    room['availability']=True
                    break
            print("Reservation cancelled")
            return
    print("Reservation not found")

def view_available_rooms():
    available_rooms = [room for room in rooms if room['availability']]
    if available_rooms:
        for room in available_rooms:
            print(room)
    else:
        print("No available rooms.")

def view_guest_details():
    if not guests:
        print("No guests found.")
        return
    print("Guest Details:")
    for guest in guests:
        print(f"ID: {guest['guest_id']}, Name: {guest['name']}, Contact: {guest['contact']}, Address: {guest['address']}, Username: {guest['username']}")

def register_guest():
    global guest_id
    name=input("Enter name")
    contact=input("Enter contact details:")
    address=input("Enter address:")
    username=input("Enter username:") 
    password=input("Enter password:")
    guest={'guest_id':guest_id,'name':name,'contact':contact,'address':address,'username':username,'password':password}
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
        print("Guest Page")
        print("1.view available rooms")
        print("2.make reservation")
        print("3.view reservation status")
        print("4.update personal information")
        print("5.cancel reservation")
        print("6.exit")
        choice=input("select an option:")
        if choice=='1':
            view_available_rooms()
        elif choice=='2':
            make_reservation()
        elif choice=='3':
            view_reservation_status(guest_id)
        elif choice=='4':
            update_personal_info(guest_id)
        elif choice=='5':
            cancel_reservation()
        elif choice=='6':
            break
        else:
            print("Invalid choice")

def view_reservation_status(guest_id):
    guest_id=str(guest_id)
    reservation_for_guest=[res for res in reservations if res['guest_id'] == guest_id]          
    if reservation_for_guest:
        for res in reservation_for_guest:
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
    