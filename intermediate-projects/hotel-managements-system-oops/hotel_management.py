class Hotel:
    sortParam = 'name'

    def __init__(self) -> None:
        # Use consistent attribute names throughout the class
        self.name = ""
        self.roomAvl = 0
        self.location = ""
        self.rating = 0
        self.pricePr = 0
        self.no_of_rooms_booked = 0

    def __lt__(self, other):
        # Return the comparison so sorting works
        return getattr(self, Hotel.sortParam) < getattr(other, Hotel.sortParam)

    # Function to change sort parameter to name
    @classmethod
    def sortByName(cls):
        cls.sortParam = 'name'

    # Function to change sort parameter to rating.
    @classmethod
    def sortByRate(cls):
        cls.sortParam = 'rating'

    # Function to change sort parameter to room availability.
    @classmethod
    def sortByRoomAvailable(cls):
        cls.sortParam = 'roomAvl'

    def __repr__(self) -> str:
        return (
            f"HotelName:{self.name}\tRoomsAvailable:{self.roomAvl}\tLocation:{self.location}"
            f"\tRating:{self.rating}\tPricePerRoom:{self.pricePr}\tRoomsBooked:{self.no_of_rooms_booked}"
        )

    def book_rooms(self, n: int) -> bool:
        """Attempt to book n rooms. If enough rooms are available, decrement availability,
        increment booked count and return True. Otherwise return False and make no change."""
        if n <= 0:
            return False
        if n <= self.roomAvl:
            self.roomAvl -= n
            self.no_of_rooms_booked += n
            return True
        return False




#User class
class User:
    def __init__(self) -> None:
        self.uname = ''
        self.uId = 0
        self.cost = 0
        self.rooms_booked = 0

    def __repr__(self) -> str:
        return f"UserName:{self.uname}\tUserId:{self.uId}\tBookingCost:{self.cost}\tRoomsBooked:{self.rooms_booked}"




# Print hotels data.
def PrintHotelData(hotels):
    for h in hotels:
        print(h)


# Sort Hotels data by name.
def SortHotelByName(hotels):
    print("SORT BY NAME:")

    Hotel.sortByName()
    hotels.sort()

    PrintHotelData(hotels)
    print()


# Sort Hotels by rating
def SortHotelByRating(hotels):
    print("SORT BY RATING:")

    Hotel.sortByRate()
    hotels.sort()
    
    PrintHotelData(hotels)
    print()


# Print Hotels for any city Location.
def PrintHotelBycity(s, hotels):
    print(f"HOTELS FOR {s} LOCATION ARE:")
    hotelsByLoc = [h for h in hotels if h.location == s]

    PrintHotelData(hotelsByLoc)
    print()



# Sort hotels by room Available.
def SortByRoomAvailable(hotels):
    print("SORT BY ROOM AVAILABLE:")
    Hotel.sortByRoomAvailable()
    hotels.sort()
    PrintHotelData(hotels)
    print()


# Print the user's data
def PrintUserData(userName, userId, bookingCost, actualBookedCounts, bookedHotelNames):
    users = []
    # Access user data and attach booking results
    for i in range(len(userName)):
        u = User()
        u.uname = userName[i]
        u.uId = userId[i]
        u.cost = bookingCost[i]
        # Use actual booked counts (0 if booking failed)
        u.rooms_booked = actualBookedCounts[i] if i < len(actualBookedCounts) else 0
        users.append(u)

    for i in range(len(users)):
        hotel_name = bookedHotelNames[i] if i < len(bookedHotelNames) else "-"
        print(users[i], "\tHotel name:", hotel_name)
    


# Functiont to solve
# Hotel Management problem
def HotelManagement(userName,
                     userId,
                     hotelName,
                     bookingCost,
                     rooms,
                     locations,
                     ratings,
                     prices,
                     bookedRooms):
    # Initialize arrays that stores
    # hotel data and user data
    hotels=[]

    # Create Objects for
    # hotel and user.

    # Initialise the data
    for i in range(len(hotelName)):
        h = Hotel()
        h.name = hotelName[i]
        h.roomAvl = rooms[i]
        h.location = locations[i]
        h.rating = ratings[i]
        h.pricePr = prices[i]
        hotels.append(h)
    
    # Initialize the data

    # Show initial hotel state
    print("Initial hotel data:")
    PrintHotelData(hotels)

    # Simulate bookings: each user i tries to book bookedRooms[i] rooms at hotels[i]
    actual_booking_costs = [0] * len(userName)
    actual_booked_counts = [0] * len(userName)
    booked_hotel_names = [""] * len(userName)
    for i in range(len(userName)):
        desired = bookedRooms[i] if i < len(bookedRooms) else 0
        hotel = hotels[i]
        success = hotel.book_rooms(desired)
        booked_hotel_names[i] = hotel.name
        if success:
            cost = desired * hotel.pricePr
            actual_booking_costs[i] = cost
            actual_booked_counts[i] = desired
            print(f"Booking successful: {userName[i]} booked {desired} room(s) at {hotel.name} for {cost}")
        else:
            actual_booking_costs[i] = 0
            actual_booked_counts[i] = 0
            print(f"Booking failed: {userName[i]} could not book {desired} room(s) at {hotel.name} (only {hotel.roomAvl} available)")

    print()

    # Call the various operations
    SortHotelByName(hotels)
    SortHotelByRating(hotels)
    PrintHotelBycity("Bangalore", hotels)
    SortByRoomAvailable(hotels)

    # Use actual_booking_costs and actual_booked_counts when printing user data
    PrintUserData(userName, userId, actual_booking_costs, actual_booked_counts, booked_hotel_names)




# Driver Code.

# ----------------------
# Interactive CLI
# ----------------------

def create_hotels(hotelName, rooms, locations, ratings, prices):
    hotels = []
    for i in range(len(hotelName)):
        h = Hotel()
        h.name = hotelName[i]
        h.roomAvl = rooms[i]
        h.location = locations[i]
        h.rating = ratings[i]
        h.pricePr = prices[i]
        hotels.append(h)
    return hotels


def print_hotels_with_index(hotels):
    print("Available hotels:")
    for idx, h in enumerate(hotels):
        print(f"[{idx}] {h}")


def find_hotel_by_input(hotels, identifier):
    """Find hotel by integer index or by name (case-insensitive). Returns hotel or None."""
    # try index
    try:
        i = int(identifier)
        if 0 <= i < len(hotels):
            return hotels[i]
    except Exception:
        pass
    # try name
    for h in hotels:
        if h.name.lower() == str(identifier).strip().lower():
            return h
    return None


def run_cli(hotels):
    users = []

    def show_menu():
        print('\n-- Hotel Management CLI --')
        print('1) List hotels')
        print('2) Sort hotels (name/rating/rooms)')
        print('3) Show hotels by city')
        print('4) Book rooms')
        print('5) Show bookings summary')
        print('6) Exit')

    while True:
        show_menu()
        choice = input('Choose an option (1-6): ').strip()
        if choice == '1':
            print_hotels_with_index(hotels)

        elif choice == '2':
            opt = input('Sort by (name/rating/rooms): ').strip().lower()
            if opt == 'name':
                Hotel.sortByName()
            elif opt == 'rating':
                Hotel.sortByRate()
            elif opt in ('rooms', 'room', 'available'):
                Hotel.sortByRoomAvailable()
            else:
                print('Unknown sort option')
                continue
            hotels.sort()
            print('Hotels sorted.')

        elif choice == '3':
            city = input('Enter city name: ').strip()
            PrintHotelBycity(city, hotels)

        elif choice == '4':
            # Booking flow
            print_hotels_with_index(hotels)
            identifier = input('Select hotel by index or exact name: ').strip()
            hotel = find_hotel_by_input(hotels, identifier)
            if hotel is None:
                print('Hotel not found. Try again.')
                continue

            try:
                n = int(input('Number of rooms to book: ').strip())
            except Exception:
                print('Invalid number.')
                continue

            if n <= 0:
                print('Please enter a positive number of rooms.')
                continue

            if hotel.book_rooms(n):
                cost = n * hotel.pricePr
                uname = input('Enter your name: ').strip() or 'Guest'
                try:
                    uid = int(input('Enter user id (integer): ').strip())
                except Exception:
                    uid = 0
                u = User()
                u.uname = uname
                u.uId = uid
                u.cost = cost
                u.rooms_booked = n
                users.append((u, hotel.name))
                print(f'Booking successful: {uname} booked {n} room(s) at {hotel.name} for {cost}')
            else:
                print(f'Booking failed: only {hotel.roomAvl} room(s) available at {hotel.name}')

        elif choice == '5':
            if not users:
                print('No bookings yet.')
            else:
                print('Bookings summary:')
                for u, hname in users:
                    print(u, '\tHotel name:', hname)

        elif choice == '6':
            print('Exiting CLI.')
            break

        else:
            print('Invalid choice, please pick 1-6.')


if __name__ == '__main__':
    # Initialize variables to stores hotels data
    hotelName = ["H1", "H2", "H3"]
    rooms = [4, 5, 6]
    locations = ["Bangalore", "Bangalore", "Mumbai"]
    ratings = [5, 5, 3]
    prices = [100, 200, 100]

    hotels = create_hotels(hotelName, rooms, locations, ratings, prices)
    print('Starting interactive Hotel Management CLI. Initial data loaded.')
    run_cli(hotels)