class Booking:
    def __init__(self, booking_id):
        self.__booking_id = booking_id
        self.__schedule = None

    def assign_schedule(self, schedule):
        self.__schedule = schedule


class Schedule:
    def __init__(self, schedule_id, date):
        self.__schedule_id = schedule_id
        self.__date = date
        self.__station = None

    @property
    def schedule_id(self):
        return self.__schedule_id

    @property
    def station(self):
        return self.__station

    def checkAvailable(self, bus):
        pass  # Logic สำหรับตรวจสอบความพร้อมใช้งาน

    def assign_station(self, station):
        self.__station = station


class Station:
    def __init__(self, station_id, station_name):
        self.__station_id = station_id
        self.__station_name = station_name
        self.__bus = None

    def assign_bus(self, bus):
        if self.__station_id >= 1:
            self.__bus = bus
            return True
        return False

    @property
    def station_name(self):
        return self.__station_name

    @property
    def bus(self):
        return self.__bus


class Bus:
    def __init__(self, bus_id, capacity):
        self.__bus_id = bus_id
        self.__capacity = capacity


class Ticket:
    ticket_counter = 1  
    
    def __init__(self):
        self.__ticket_id = Ticket.ticket_counter 
        Ticket.ticket_counter += 1
        self.__schedule = []

    def assign_schedule(self, schedule):
        self.__schedule.append(schedule)

    @property
    def ticket_id(self):
        return self.__ticket_id
    



bus = Bus(1, 50)
station1 = Station(1, "EE")
station1.assign_bus(bus)
schedule1 = Schedule(1, "2025-01-31")
schedule1.assign_station(station1)
ticket = Ticket()
ticket1 = Ticket()
print(ticket1.ticket_id)

