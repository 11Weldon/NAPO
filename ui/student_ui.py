from core.logic import get_student_grades, get_student_attendance, get_student_schedule
from core.notifications import NotificationManager

notification_manager = NotificationManager()
def student_menu(user):
    while True:
        print("\n--- Student Menu ---")
        print("1. View Grades")
        print("2. View Attendance")
        print("3. View Schedule")
        print("4. View Notifications")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            view_grades_menu(user)
        elif choice == '2':
            view_attendance_menu(user)
        elif choice == '3':
            view_schedule_menu(user)
        elif choice == '4':
            view_notifications_menu(user)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")


def view_grades_menu(user):
    print("\n--- View Grades ---")
    grades = get_student_grades(user.id)
    if grades:
        for grade in grades:
            print(f"Subject ID: {grade.subject_id}, Grade: {grade.value}, Date: {grade.date}")
    else:
        print("No grades found")


def view_attendance_menu(user):
    print("\n--- View Attendance ---")
    attendance = get_student_attendance(user.id)
    if attendance:
      for item in attendance:
        print(f"Subject ID: {item.subject_id}, Status: {item.status}, Date: {item.date}")
    else:
        print("No attendance found")

def view_schedule_menu(user):
    print("\n--- View Schedule ---")
    schedule = get_student_schedule(user.id)
    if schedule:
        for item in schedule:
          print(f"Date: {item.date}, Time: {item.time}, Subject ID: {item.subject_id}, Group ID: {item.group_id}")
    else:
      print("No schedule found")


def view_notifications_menu(user):
    print("\n--- View Notifications ---")
    notifications = notification_manager.get_user_notifications(user.id)
    if notifications:
        for notification in notifications:
            print(f"Message: {notification.message}, Date: {notification.date}")
    else:
        print("No notifications found")