# รหัส นศ. ชื่อ นศ. 
        
class AppointmentScheduler:
    def __init__(self):
        self.__appointments = []
        self.__evnet_list = []
    def edit_appointment(self):    
            # ให้แก้ไข การนัดหมาย/กิจกรรม โดยใช้ title หรือ location
        pass            
    def view_appointments(self):
        for appointment in self.__appointments:
            for j in appointment.member:
                for e in j.person:
                    print(f"{appointment.day}{appointment.title}{appointment.date}{appointment.location}{e.name}")
        
    def delete_appointment(self, title):    # ให้ลบ การนัดหมาย/กิจกรรม โดยใช้ title
        pass

    def add_attendance(self, title, member):    # ให้เพิ่ม ผู้ได้รับการนัดหมาย สำหรับ การนัดหมายรายครั้ง และ การนัดหมายรายสัปดาห์
        pass

    def show_person_in_appointment(self, person):    # ให้ค้นหาการนัดหมายรายบุคคล โดยใช้ชื่อ
        pass
    def add_member_list(self,person):
        self.__person_list.append(person)
    def add_appointments_inapp(self,appointment):
        self.__appointments.append(appointment)
    def send_notifications(self, title, message):    # ให้แจ้ง Notification โดยใช้การนัดหมาย
        pass
class Appointmets:
    def __init__(self,title,location,date):
        self.__title = title
        self.__date = date
        self.__location = location
        self.__day = "การนัดหมายแบบรายครั้ง"
        self.__member = []
    @property
    def id(self):
        return self.__id
    @property
    def day(self):
        return self.__day
    @property
    def title(self):
        return self.__title
    @property
    def date(self):
        return self.__date
    @property
    def location(self):
        return self.__location
    def add_member(self,member):
        
        self.__member.append(member)
    @property
    def member(self):
        return self.__member

class AppoinmetsDay(Appointmets):
    def ___init__(self,title,date,location):
        super().__init__(title,date,location)
        self.__weekly = "การนัดหมาย ประเภท รายสัปดาห์"
    @property
    def weekly(self):
        return self.__weekly
class AppoimentsWeekly(Appointmets):
    def ___init__(self,title,date,location):
        super().__init__(title,date,location)
class Appoinmetn_list:
    def __init__(self):
        self.__appoinment_list = []
    def add_appoinment_list(self,appoinmet):
        self.__appoinment_list.append(appoinmet)
class Event(Appointmets):
    def __init__(self,title,date,location):
        super().__init__(title,date,location)
        
class Member:
    def __init__(self):
        self.__person = []
    @property
    def person(self):
        return self.__person
    def add_member(self,person):
        self.__person.append(person)
class Person(Appoinmetn_list):
    def __init__(self,name,detail):
        super().__init__()
        self.__name = name
        self.__detail = detail
    @property 
    def name(self):
        return self.__name
    @property 
    def detail(self):
        return self.__detail
    def add_addinment(self,appoinmet):
        super().add_appoinment_list(appoinmet)

#     def __init__(self):
#         super().__init__()
#     def add_appoments(self,appoment):
#         super().add_appoiment_list(appoment)

    
app = AppointmentScheduler()
# app1 = AppoinmetsDay("Team Meeting #1")
app2 = Appoinmetn_list()
person1 = Person("JOhn Doe","john.doe@example.com")
person2 = Person("jane Smith","jane.smith@example.com")
person3 = Person("Robert johnson","robert.johnson@example.com" "08-1234-5678")
person4 = Person("Emily Davis","emily.davis@example.com" "08-3456-7890")
app1 = Appointmets("Team Meeting #1","Room A","2024-03-15")
app2 = Appointmets("Team Meeting #2","Room B","2024-03-17")
app3 = AppoimentsWeekly("Weekly Meeting #2","Room C","Wednesday")
evn =  Event("Company Party","Conference Room","2024-03-17")
evn2 = Event("Company Visit","Conference Room","2024-03-17")

# person1.add_addinment(app)
member1 = Member()
member1.add_member(person1)
member1.add_member(person2)
member1.add_member(person3)
member1.add_member(person4)

app1.add_member(member1)
app1.add_member(member1)
app2.add_member(member1)
app.add_appointments_inapp(app1)
app.add_appointments_inapp(app2)




# # ให้เขียนโปรแกรมเพื่อเพิ่มสมาชิก ตามรายละเอียดด้านล่าง
# Add Member
# "John Doe", "john.doe@example.com"
# "Jane Smith", "jane.smith@example.com"
# "Robert Johnson", "robert.johnson@example.com", "08-1234-5678"
# "Emily Davis", "emily.davis@example.com", "08-3456-7890"

# # # Test Case 1 : Add Appointment เพิ่มข้อมูล กิจกรรม  และเพิ่มข้อมูลการนัดหมาย 
# 1 : title="Team Meeting #1", location="Room A" , date="2024-03-15", Jane Smith, Robert Johnson,  Emily Davis
# 2 : title="Team Meeting #2", location="Room B" , date="2024-03-17", Jane Smith, Robert Johnson และ Emily Davis
# 3 : title="Weekly Meeting", location="Room C" , day_of_week="Wednesday"
# # Activity
# 4 : title="Company Party", location="Conference Room", date="2024-03-17"
# 5 : title="Company Visit", location="Conference Room", date="2024-03-17"

# # Output Expect
# # Topic : Team Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis
# # Topic : Team Meeting #2 Location : Room B on 2024-03-17 Attn: Jane Smith,John Doe,Emily Davis
# # Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis
# # Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# # Activity, Topic : Company Visit Location : Conference Room on 2024-03-17


print("Test Case 1 : Add Appointment เพิ่มข้อมูล กิจกรรม  และเพิ่มข้อมูลการนัดหมาย ")
app.view_appointments()            # แสดง Appointment ทั้งหมด
print()

# # # Test Case 2 : Edit Appointment แก้ไข การนัดหมาย/กิจกรรม 
# # เปลี่ยนชื่อ การนัดหมาย รายครั้ง #1 จาก “Team Meeting #1” เป็น “Team B Meeting #1”
# # Output Expect
# # Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis
# # Topic : Team Meeting #2 Location : Room C on 2024-03-17 Attn: Jane Smith,John Doe,Emily Davis
# # Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis
# # Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# # Activity, Topic : Company Visit Location : Conference Room on 2024-03-17
# print("Test Case 2 : Edit Appointment แก้ไข การนัดหมาย/กิจกรรม ")
# app.edit_appointment(title="Team Meeting #1",to="Team B Meeting #1")
# app.edit_appointment(location="Room B",to="Room C")
# app.view_appointments()            # แสดง Appointment ทั้งหมด
# print()


# # # Test Case 3 : Delete Appointment ลบ การนัดหมาย/กิจกรรม โดยใช้ topic “Team Meeting #2” 
# # Output Expect
# # Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis
# # Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis
# # Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# # Activity, Topic : Company Visit Location : Conference Room on 2024-03-17
# print("Test Case 3 : Delete Appointment ลบ การนัดหมาย/กิจกรรม โดยใช้ topic “Team Meeting #2”")
# app.delete_appointment(title="Team Meeting #2")
# app.view_appointments()            # แสดง Appointment ทั้งหมด
# print()

# # # Test Case 4 : Add Attendance ผู้ได้รับการนัดหมาย สำหรับ การนัดหมายรายครั้ง และ การนัดหมายรายสัปดาห์ ดังนี้
# # -	การนัดหมาย รายครั้ง #1 (“Team B Meeting #1”) เพิ่ม John Doe
# # -	การนัดหมาย รายสัปดาห์ “Weekly Meeting” เพิ่ม Jane Smith
# # Output Expect
# # Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis,John Doe
# # Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis,Jane Smith
# # Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# # Activity, Topic : Company Visit Location : Conference Room on 2024-03-17
# print("Test Case 4 : Add Attendance ผู้ได้รับการนัดหมาย สำหรับ การนัดหมายรายครั้ง และ การนัดหมายรายสัปดาห์")
# app.add_attendance("Team B Meeting #1", john)
# app.add_attendance("Weekly Meeting", jane)
# app.view_appointments()            # แสดง Appointment ทั้งหมด
# print()

# # # Test Case 5 : Search Attendance ค้นหาการนัดหมายรายบุคคล โดยใช้ชื่อ “Robert Johnson” 
# # Output Expect
# # Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis,John Doe
# # Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis,Jane Smith
# print("Test Case 5 : Search Attendance ค้นหาการนัดหมายรายบุคคล โดยใช้ชื่อ Robert Johnson")
# app.show_person_in_appointment(john)
# print()

# # # Test Case 6 : แจ้ง Notification โดยใช้การนัดหมาย “Team B Meeting #1”
# # Output Expect
# # Sending email notification to: jane.smith@example.com with message : invite for meeting
# # Sending email notification to: john.doe@example.com with message : invite for meeting
# # Sending SMS notification to : 08-3456-7890 with message : invite for meeting
# # Sending email notification to: john.doe@example.com with message : invite for meeting
# print("""Test Case 6 : แจ้ง Notification โดยใช้การนัดหมาย “Team B Meeting #1""")
# app.send_notifications("Team B Meeting #1","invite for meeting")


