class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = {}

class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully!")

    def mark_attendance(self, student_id, date):
        if student_id in self.students:
            student = self.students[student_id]
            student.attendance[date] = True
            print(f"Attendance marked for {student.name} on {date}")
        else:
            print("Student not found!")

    def view_attendance(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Attendance for {student.name}:")
            for date, attended in student.attendance.items():
                status = "Present" if attended else "Absent"
                print(f"{date}: {status}")
        else:
            print("Student not found!")

# Creating an instance of the AttendanceSystem
attendance_system = AttendanceSystem()

# Adding students
attendance_system.add_student("S001", "Suvaathii")
attendance_system.add_student("S002", "Saranraj")
attendance_system.add_student("S003", "Keerthanan")

# Marking attendance
attendance_system.mark_attendance("S001", "2023-08-25")
attendance_system.mark_attendance("S002", "2023-08-25")
attendance_system.mark_attendance("S003", "2023-08-25")

# Viewing attendance
attendance_system.view_attendance("S001")
attendance_system.view_attendance("S002")
attendance_system.view_attendance("S003")