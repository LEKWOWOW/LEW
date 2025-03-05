class Booking:
    def __init__(self,booking_id):
        self.__booking_id = booking_id
        self.__schedul = None
    def assing_Schedul(self,schedul):
        self.__schedul =schedul
class Schedul:
    def __init__(self,schedul_id,date):
        self.__schedul_id  = schedul_id
        self.__date = date 
        self.__station = None
    @property
    def schedul_id(self):
        return self.__schedul_id
    @property
    def station(self):
        return self.__station
    def checkAvailable(self,bus): 
        pass
    def assing_station(self,station):
        self.__station =station
    
class Station:
    def __init__(self,station_id,station_name):
        self.__station_id = station_id
        self.__station_name = station_name
        self.__bus = None
    def assing_bus(self,bus):
        if self.__station_id >=1:
            return self.__bus == bus
        return False
    @property
    def station_name(self):
        return self.__station_name
    
class Bus:
    def __init__(self,bus_id,capacity):
        self.__bus_id = bus_id
        self.__capacity = capacity
        self.__seat = [Seat(i) for i in range(1,capacity + 1)]
class Seat:
    def __init__(self,seat_id):
        self.__seat_id = seat_id
        self.__available = True
    @property
    def abailable(self):
        return self.__available
    def booking_seat(self):
        if self.__available:
            self.__available = False
            return True
        return False
class Ticket:
    def __init__(self,ticket_id):
        self.__ticket_id = ticket_id
bus = Bus(1)
station1 = Station(1,"หมอชิต")
station1.assing_bus(bus)
schedul1  = Schedul(1,"2025-31-1")
schedul1.assing_station(station1)
print(schedul1.station.station_name)