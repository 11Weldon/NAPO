from core.logic import add_grade, add_attendance, get_teacher_report, get_teacher_schedule
def teacher_menu(user):
    while True:
        print("\n--- Teacher Menu ---")
        print("1. Add Grade")
        print("2. Add Attendance")
        print("3. View Report")
        print("4. View Schedule")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_grade_menu()
        elif choice == '2':
            add_attendance_menu()
        elif choice == '3':
            view_report_menu(user)
        elif choice == '4':
           view_schedule_menu(user)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")


def add_grade_menu():
    print("\n--- Add Grade ---")
    student_id = input("Enter student ID: ")
    subject_id = input("Enter subject ID: ")
    value = input("Enter grade value: ")
    grade_data = {"student_id": int(student_id), "subject_id": int(subject_id), "value": int(value)}
    grade = add_grade(grade_data)
    if grade:
      print(f"Grade added successfully for student {student_id} on subject {subject_id} with value {value}")
    else:
      print("Failed to add grade")

def add_attendance_menu():
    print("\n--- Add Attendance ---")
    student_id = input("Enter student ID: ")
    subject_id = input("Enter subject ID: ")
    status = input("Enter attendance status (present, absent): ")
    attendance_data = {"student_id": int(student_id), "subject_id": int(subject_id), "status": status}
    attendance = add_attendance(attendance_data)
    if attendance:
      print(f"Attendance added successfully for student {student_id} on subject {subject_id} with status {status}")
    else:
      print("Failed to add attendance")

def view_report_menu(user):
    print("\n--- View Report ---")
    subject_id = input("Enter subject ID: ")
    report = get_teacher_report(user.id, int(subject_id))
    if report:
      for grade in report:
        print(f"Student ID: {grade.student_id}, Grade: {grade.value}, Date: {grade.date}")
    else:
      print("Report not found")

def view_schedule_menu(user):
  print("\n--- View Schedule ---")
  schedule = get_teacher_schedule(user.id)
  if schedule:
    for item in schedule:
      print(f"Date: {item.date}, Time: {item.time}, Subject ID: {item.subject_id}, Group ID: {item.group_id}")
  else:
    print("No schedule found")