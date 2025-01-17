from core.roles import Role
from ui.admin_ui import admin_menu
from ui.teacher_ui import teacher_menu
from ui.student_ui import student_menu
from core.logic import get_user
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            user_id = input("Enter your user ID: ")
            try:
                user = get_user(int(user_id))
                if user:
                    # print(f"User type: {type(user)}, User role: {user.role}")  # Debug
                    if user.role.value == Role.ADMIN.value:
                        admin_menu()
                    elif user.role.value == Role.TEACHER.value:
                        teacher_menu(user)
                    elif user.role.value == Role.STUDENT.value:
                        student_menu(user)
                    else:
                        print("Invalid role.")
                else:
                    print("User not found")
            except ValueError:
                print("Invalid user ID, please enter a number")
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()