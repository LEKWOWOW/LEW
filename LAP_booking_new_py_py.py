class Seat:
    def __init__(self, seat_number):
        self.__seat_number = seat_number
        self.__available = True
    
    @property
    def seat_number(self):
        return self.__seat_number
    
    @property
    def available(self):
        return self.__available
    
    def bookSeat(self):
        if self.__available:
            self.__available = False
            return True
        return False
    
    def releaseSeat(self):
        self.__available = True

class Bus:
    def __init__(self, bus_id, bus_number, capacity):
        self.__bus_id = bus_id
        self.__bus_number = bus_number
        self.__capacity = capacity
        self.__seats = [Seat(i) for i in range(1, capacity + 1)]
    
    def assignRoute(self, route):
        self.route = route
    @property
    def bus_id(self):
        return self.__bus_id
    @property
    def bus_number(self):
        return self.__bus_number
    @property
    def capacity(self):
        return self.__capacity
    @property
    def seats(self):
        return self.__seats
    def checkAvailability(self):
        return any(seat.available for seat in self.seats)
    
    def bookSeat(self):
        for seat in self.seats:
            if seat.bookSeat():
                return seat.seat_number
        return None
    
    def releaseSeat(self, seat_number):
        for seat in self.seats:
            if seat.seat_number == seat_number:
                seat.releaseSeat()
                return True
        return False
    def add_bus(bus_id,bus_number,capacity):
        bus = Bus(bus_id,bus_number, capacity)
        return bus 

class Schedule:
    def __init__(self, schedule_id, departure_time, arrival_time, bus,price,station):
        self.__schedule_id = schedule_id
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__bus = bus
        self.__price  = price
        self.__station = station
    @property
    def schedule_id(self):
        return self.__schedule_id
    @property
    def departure_time(self):
        return self.__departure_time
    @property
    def arrival_time(self):
        return self.__arrival_time
    @property
    def bus(self):
        return self.__bus
    @property
    def price(self):
         return self.__price
    @property
    def station(self):
        return self.__station 
    def checkAvailability(self):
        return self.bus.checkAvailability()
    def calculateprice(self):
        n = 20 
        # if self.station.station_number >= 2:
        #     return n 
        return self.__station.station_number * n 
class Booking:
    def __init__(self, booking_id, booking_date, schedule):
        self.__booking_id = booking_id
        self.__booking_date = booking_date
        self.__schedule = schedule
        self.__seat_number = None
    @property
    def booking_id(self):
        return self.__booking_id
    @property
    def station(self):
        return self.__station
    @property
    def schedule(self):
        return self.__schedule
    
    def addTicket(self):
        if self.schedule.checkAvailability():
            self.seat_number = self.schedule.bus.bookSeat()
            return True
        return False
    
    def cancelBooking(self):
        if self.seat_number:
            self.schedule.bus.releaseSeat(self.seat_number)
            self.seat_number = None
            return True
        return False
   
class Station:
    def __init__(self, station_number, station_name):
        self.__station_number  = station_number
        self.__station_name = station_name
        self__bus = None
    @property   
    def station_number(self):
        return self.__station_number
    @property
    def station_name(self):
        return self.__station_name 
def bus(self):
    return self.__bus
def assign_bus(self):
    pass
bus1  = Bus.add_bus(1,"eee",40)
station = Station(1,"หมอชิต2")
station1 = Station(3,"อนุสาวรีย์")
schedule1 = Schedule("S1", "2025-02-20 08:00", "2025-02-20 12:00", bus1,120,station)
schedule2 = Schedule("S2", "2025-02-20 08:00", "2025-02-20 12:00", bus1,140,station1)

bookings = {}

def book_ticket(booking_id, booking_date, schedule):
    if booking_id in bookings:
        return f"Booking ID {booking_id} already exists."
    
    if schedule.checkAvailability():
        booking = Booking(booking_id, booking_date, schedule)
        if booking.addTicket():
            bookings[booking_id] = booking
            return f"Booking Confirmed: ID {booking_id}, Seat {booking.seat_number}, Bus {schedule.bus.bus_number},schedule :{schedule.schedule_id},price| :{schedule.calculateprice()}"
        
        else:
            return "No available seats."
    else:
        return "No available schedule."
schedule_list = [schedule1,schedule2]
def add_data():
    return   print(book_ticket("01", "2025-02-20", schedule2)),print(book_ticket("02", "2025-02-20", schedule1))
            
    # (book_ticket("01", "2025-02-20", schedule2))
    # (book_ticket("02", "2025-02-20", schedule2))
    # (book_ticket("03", "2025-02-20", schedule2))
    # (book_ticket("04", "2025-02-20", schedule1))
    # (book_ticket("05", "2025-02-20", schedule1))
    # (book_ticket("06", "2025-02-20", schedule1))
    # (book_ticket("07", "2025-02-20", schedule1))
    # (book_ticket("08", "2025-02-20", schedule1))
    # (book_ticket("09", "2025-02-20", schedule1))
    # (book_ticket("10", "2025-02-20", schedule1))
    # (book_ticket("01", "2025-02-20", schedule1))
def test_case():
     add_data()
test_case()
                    
