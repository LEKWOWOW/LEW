class Student:
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name

    def get_student_id(self):
        return self.__student_id

    def get_student_name(self):
        return self.__student_name


class Subject:
    def __init__(self, subject_id, subject_name, credit):
        self.__subject_id = subject_id
        self.__subject_name = subject_name
        self.__credit = credit
        self.__teacher = None
        self.__enrollments = []

    def get_subject_id(self):
        return self.__subject_id

    def get_subject_name(self):
        return self.__subject_name

    def get_credit(self):
        return self.__credit

    def assign_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.__teacher = teacher
            return "Done"
        return "Error"

    def get_teacher(self):
        return self.__teacher

    def get_enrollments(self):
        return self.__enrollments


class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.__teacher_id = teacher_id
        self.__teacher_name = teacher_name

    def get_teacher_id(self):
        return self.__teacher_id

    def get_teacher_name(self):
        return self.__teacher_name


class Enrollment:
    def __init__(self, student, subject):
        self.__student = student
        self.__subject = subject
        self.__grade = None

    def get_student(self):
        return self.__student

    def get_subject(self):
        return self.__subject

    def assign_grade(self, grade):
        if self.__grade is not None:
            return "Error"
        self.__grade = grade
        return "Done"

    def get_grade(self):
        return self.__grade


# List for storing instances
student_list = []
subject_list = []
teacher_list = []
enrollment_list = []


# Helper function
def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    return grade_mapping.get(grade, 0)


# Functions
def search_subject_by_id(subject_id):
    for subject in subject_list:
        if subject.get_subject_id() == subject_id:
            return subject
    return None


def search_student_by_id(student_id):
    for student in student_list:
        if student.get_student_id() == student_id:
            return student
    return None


def enroll_to_subject(student, subject):
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return "Error"
    if any(enrollment.get_student() == student for enrollment in subject.get_enrollments()):
        return "Already Enrolled"
    enrollment = Enrollment(student, subject)
    subject.get_enrollments().append(enrollment)
    enrollment_list.append(enrollment)
    return "Done"


def drop_from_subject(student, subject):
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return "Error"
    for enrollment in subject.get_enrollments():
        if enrollment.get_student() == student:
            subject.get_enrollments().remove(enrollment)
            enrollment_list.remove(enrollment)
            return "Done"
    return "Not Found"


def list_student_enrolled_in_subject(subject_id):
    subject = search_subject_by_id(subject_id)
    if subject is None:
        return "Subject not found"
    result = {}
    for enrollment in subject.get_enrollments():
        student = enrollment.get_student()
        result[student.get_student_id()] = student.get_student_name()
    return result


def search_student_enrolled_in_subject(subject):
    students = []
    for enrollment in enrollment_list:
        if enrollment.get_subject() == subject:
            students.append(enrollment.get_student())
    return students


def get_teacher_teach(subject):
    return subject.get_teacher()

def get_no_of_student_enrolled(subject):
    if not isinstance(subject, Subject):
        return "Error"
    enrolled_students = search_student_enrolled_in_subject(subject)
    return len(enrolled_students)


def search_subject_that_student_enrolled(student):
    if not isinstance(student, Student):
        return "Error"
    enrolled_subjects = []
    for enrollment in enrollment_list:
        if enrollment.get_student() == student:
            enrolled_subjects.append(enrollment.get_subject())
    return enrolled_subjects


def search_enrollment_subject_student(subject, student):
    if not isinstance(subject, Subject) or not isinstance(student, Student):
        return "Error"
    for enrollment in enrollment_list:
        if enrollment.get_subject() == subject and enrollment.get_student() == student:
            return enrollment
    return "Enrollment not found"

# Function to assign a grade to a student's enrollment in a subject
def assign_grade(student, subject, grade):
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return "Error"
    for enrollment in enrollment_list:
        if enrollment.get_student() == student and enrollment.get_subject() == subject:
            return enrollment.assign_grade(grade)  # Use the `assign_grade` method from the Enrollment class
    return "Enrollment not found"

def get_student_record(student):
    if not isinstance(student, Student):
        return "Error"
    record = {}
    for enrollment in enrollment_list:
        if enrollment.get_student() == student:
            subject = enrollment.get_subject()
            grade = enrollment.get_grade()
            record[subject.get_subject_id()] = [subject.get_subject_name(), grade]
    return record


def get_student_GPS(student):
    if not isinstance(student, Student):
        return "Error"
    total_points = 0
    total_subjects = 0
    for enrollment in enrollment_list:
        if enrollment.get_student() == student:
            grade = enrollment.get_grade()
            if grade is not None:
                total_points += grade_to_count(grade)
                total_subjects += 1
    if total_subjects == 0:
        return 0  # Return 0 if the student is not enrolled in any subjects or has no grades
    return total_points / total_subjects  # Return GPA



# Create instances for testing
def create_instance():
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 3))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 3))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])


# Register students for subjects
def register():
    enroll_to_subject(student_list[0], subject_list[0])  # 001 -> CS101
    enroll_to_subject(student_list[0], subject_list[1])  # 001 -> CS102
    enroll_to_subject(student_list[0], subject_list[2])  # 001 -> CS103
    enroll_to_subject(student_list[1], subject_list[0])  # 002 -> CS101
    enroll_to_subject(student_list[1], subject_list[1])  # 002 -> CS102
    enroll_to_subject(student_list[1], subject_list[2])  # 002 -> CS103
    enroll_to_subject(student_list[2], subject_list[0])  # 003 -> CS101
    enroll_to_subject(student_list[2], subject_list[1])  # 003 -> CS102
    enroll_to_subject(student_list[2], subject_list[2])  # 003 -> CS103
    enroll_to_subject(student_list[3], subject_list[0])  # 004 -> CS101
    enroll_to_subject(student_list[3], subject_list[1])  # 004 -> CS102
    enroll_to_subject(student_list[4], subject_list[0])  # 005 -> CS101
    enroll_to_subject(student_list[4], subject_list[2])  # 005 -> CS103
    enroll_to_subject(student_list[5], subject_list[1])  # 006 -> CS102
    enroll_to_subject(student_list[5], subject_list[2])  # 006 -> CS103
    enroll_to_subject(student_list[6], subject_list[0])  # 007 -> CS101
    enroll_to_subject(student_list[7], subject_list[1])  # 008 -> CS102
    enroll_to_subject(student_list[8], subject_list[2])  # 009 -> CS103


create_instance()
register()


## Test Case #1 : test enroll_to_subject complete ###
student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print(student_enroll)
print("")


### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
print("Answer : Error")
print(enroll_to_subject('66010001','CS101'))
print("")

### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
print("Answer : Already Enrolled")
print(enroll_to_subject(student_list[0], subject_list[0]))
print("")

### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
print("Answer : Error")
print(drop_from_subject('66010001', 'CS101'))
print("")

### Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
print("Answer : Not Found")
print(drop_from_subject(student_list[8], subject_list[0]))
print("")

### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
drop_from_subject(student_list[0], subject_list[0])
print(list_student_enrolled_in_subject(subject_list[0].get_subject_id()))
print("")

## Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enrolled_in_subject(subject_list[0])
print([i.get_student_id() for i in lst])
print("")

### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
print("Answer : 5")
print(get_no_of_student_enrolled(subject_list[0]))
print("")

### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
print("Answer : ['CS102','CS103']")
lst = search_subject_that_student_enrolled(student_list[0])
print([i.get_subject_id() for i in lst])
print("")

### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
print("Answer : Mr. Welsh")
print(get_teacher_teach(subject_list[0]).get_teacher_name())
print("")

### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
print("Answer : CS101 66010002")
enroll = search_enrollment_subject_student(subject_list[0],student_list[1])
print(enroll.get_subject().get_subject_id(), enroll.get_student().get_student_id())
print("")

### Test case #12 : assign_grade
print("Test case #12 assign_grade")
print("Answer : Done")
assign_grade(student_list[1],subject_list[0],'A')
assign_grade(student_list[1],subject_list[1],'B')
print(assign_grade(student_list[1],subject_list[2],'C'))
print("")

### Test case #13 : get_student_record
print("Test case #13 get_student_record")
print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print(get_student_record(student_list[1]))
print("")

### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
print("Answer : 3.0")
print(get_student_GPS(student_list[1]))
