# รหัส นศ. ชื่อ นศ. 
        
class AppointmentScheduler:
    def __init__(self):
        self.appointments = []
class Appoinmetn:
    def __init___(self,name_appoinment,date,loacation,detail):
        self.__name_appoinment = name_appoinment
        self.__date = date 
        self.__location = loacation 
        self.__detail = detail
    @property
    def name_appoinment (self):
        return self.__name_appoinment
    @property
    def date(self):
        return self.__date
    @property
    def location(self):
        return self.__location
    @property
    def detail(self):
        return self.__detail
    
    
class AppoimentDay(Appoinmetn):
    def __init__(self,name_appoinment,date,location,detail):
        super().__init__(name_appoinment,date,location,detail)
    
class AppoimentWeekly(Appoinmetn):
    def __init__(self,name_appoinment,date,location,detail):
        super().__init__(name_appoinment,date,location,detail)
# class Appoiment_list:
#     def __init__(self):
#         self.__appoiment_list = []
    
#     # def add_appoiment_list(self,appoment):
#     #     self.__appoiment_list.append(appoment)
#     @property
#     def appoiment(self):
#         return self.__appoiment_list
# class Appoinmetn_list():
#     def __init__(self):
#         self.__appoinments = []
#     def add_appoiment_list(self,appoment):
#         self.__appoinments.append(appoment)
#     @property
#     def apponments(self):
#         return self.__appoinments
    
# class Peson(Appoiment_list):
#     def __init__(self,name):
#         super().__init__()
#         self.__name = name
#     def add_appoments(self,appoinment):
#         super.add_appoiment_list(appoinment)
    
    # def add_appoiment_list(self, appoment):
    #     return super().add_appoiment_list(appoment)
     
        
    
    # def add_appointment(self, appointment):
    #     self.appointments.append(appointment)    

    def edit_appointment(self):     # ให้แก้ไข การนัดหมาย/กิจกรรม โดยใช้ title หรือ location
        pass            

    def view_appointments(self):
        
        for appointment in self.appointments:
            print(appointment)
        pass
    def delete_appointment(self, title):    # ให้ลบ การนัดหมาย/กิจกรรม โดยใช้ title
        pass

    def add_attendance(self, title, member):    # ให้เพิ่ม ผู้ได้รับการนัดหมาย สำหรับ การนัดหมายรายครั้ง และ การนัดหมายรายสัปดาห์
        pass

    def show_person_in_appointment(self, person):    # ให้ค้นหาการนัดหมายรายบุคคล โดยใช้ชื่อ
        pass

    def send_notifications(self, title, message):    # ให้แจ้ง Notification โดยใช้การนัดหมาย
        pass
gg = AppoimentWeekly("To","e","t","g")

# app = AppointmentScheduler()
# ให้เขียนโปรแกรมเพื่อเพิ่มสมาชิก ตามรายละเอียดด้านล่าง
# Add Member
# "John Doe", "john.doe@example.com"
# "Jane Smith", "jane.smith@example.com"
# "Robert Johnson", "robert.johnson@example.com", "08-1234-5678"
# "Emily Davis", "emily.davis@example.com", "08-3456-7890"

# # Test Case 1 : Add Appointment เพิ่มข้อมูล กิจกรรม  และเพิ่มข้อมูลการนัดหมาย 
# 1 : title="Team Meeting #1", location="Room A" , date="2024-03-15", Jane Smith, Robert Johnson,  Emily Davis
# 2 : title="Team Meeting #2", location="Room B" , date="2024-03-17", Jane Smith, Robert Johnson และ Emily Davis
# 3 : title="Weekly Meeting", location="Room C" , day_of_week="Wednesday"
# Activity
# 4 : title="Company Party", location="Conference Room", date="2024-03-17"
# 5 : title="Company Visit", location="Conference Room", date="2024-03-17"

# Output Expect
# Topic : Team Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis
# Topic : Team Meeting #2 Location : Room B on 2024-03-17 Attn: Jane Smith,John Doe,Emily Davis
# Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis
# Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# Activity, Topic : Company Visit Location : Conference Room on 2024-03-17


# print("Test Case 1 : Add Appointment เพิ่มข้อมูล กิจกรรม  และเพิ่มข้อมูลการนัดหมาย ")
# app.view_appointments()            # แสดง Appointment ทั้งหมด
# print()

# # Test Case 2 : Edit Appointment แก้ไข การนัดหมาย/กิจกรรม 
# เปลี่ยนชื่อ การนัดหมาย รายครั้ง #1 จาก “Team Meeting #1” เป็น “Team B Meeting #1”
# Output Expect
# Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis
# Topic : Team Meeting #2 Location : Room C on 2024-03-17 Attn: Jane Smith,John Doe,Emily Davis
# Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis
# Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# Activity, Topic : Company Visit Location : Conference Room on 2024-03-17
# print("Test Case 2 : Edit Appointment แก้ไข การนัดหมาย/กิจกรรม ")
# app.edit_appointment(title="Team Meeting #1",to="Team B Meeting #1")
# app.edit_appointment(location="Room B",to="Room C")
# app.view_appointments()            # แสดง Appointment ทั้งหมด
# print()


# # Test Case 3 : Delete Appointment ลบ การนัดหมาย/กิจกรรม โดยใช้ topic “Team Meeting #2” 
# Output Expect
# Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis
# Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis
# Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# Activity, Topic : Company Visit Location : Conference Room on 2024-03-17
# print("Test Case 3 : Delete Appointment ลบ การนัดหมาย/กิจกรรม โดยใช้ topic “Team Meeting #2”")
# app.delete_appointment(title="Team Meeting #2")
# app.view_appointments()            # แสดง Appointment ทั้งหมด
# print()

# # Test Case 4 : Add Attendance ผู้ได้รับการนัดหมาย สำหรับ การนัดหมายรายครั้ง และ การนัดหมายรายสัปดาห์ ดังนี้
# -	การนัดหมาย รายครั้ง #1 (“Team B Meeting #1”) เพิ่ม John Doe
# -	การนัดหมาย รายสัปดาห์ “Weekly Meeting” เพิ่ม Jane Smith
# Output Expect
# Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis,John Doe
# Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis,Jane Smith
# Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# Activity, Topic : Company Visit Location : Conference Room on 2024-03-17
# print("Test Case 4 : Add Attendance ผู้ได้รับการนัดหมาย สำหรับ การนัดหมายรายครั้ง และ การนัดหมายรายสัปดาห์")
# app.add_attendance("Team B Meeting #1", john)
# app.add_attendance("Weekly Meeting", jane)
# app.view_appointments()            # แสดง Appointment ทั้งหมด
# print()

# # Test Case 5 : Search Attendance ค้นหาการนัดหมายรายบุคคล โดยใช้ชื่อ “Robert Johnson” 
# Output Expect
# Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis,John Doe
# Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis,Jane Smith
# print("Test Case 5 : Search Attendance ค้นหาการนัดหมายรายบุคคล โดยใช้ชื่อ Robert Johnson")
# app.show_person_in_appointment(john)
# print()

# # Test Case 6 : แจ้ง Notification โดยใช้การนัดหมาย “Team B Meeting #1”
# Output Expect
# Sending email notification to: jane.smith@example.com with message : invite for meeting
# Sending email notification to: john.doe@example.com with message : invite for meeting
# Sending SMS notification to : 08-3456-7890 with message : invite for meeting
# Sending email notification to: john.doe@example.com with message : invite for meeting
# print("""Test Case 6 : แจ้ง Notification โดยใช้การนัดหมาย “Team B Meeting #1""")
# app.send_notifications("Team B Meeting #1","invite for meeting")


