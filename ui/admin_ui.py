from core.logic import create_user, create_subject, create_schedule, create_semester, get_all_users, get_all_subjects, \
    get_all_semesters, create_group, get_all_groups, assign_subject_to_semester
from core.roles import Role
from core.db import get_session
from core.models import User, Subject, Group, Schedule, Semester
from datetime import datetime


def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Manage Users")
        print("2. Manage Groups")
        print("3. Manage Subjects")
        print("4. Manage Schedule")
        print("5. Manage Semesters")
        print("6. Assign Subject to Semester")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            manage_users_menu()
        elif choice == '2':
            manage_groups_menu()
        elif choice == '3':
            manage_subjects_menu()
        elif choice == '4':
            manage_schedule_menu()
        elif choice == '5':
            manage_semesters_menu()
        elif choice == '6':
            assign_subject_to_semester_menu()
        elif choice == '7':
            break
        else:
            print("Invalid choice.")


def manage_users_menu():
    while True:
        print("\n--- Manage Users Menu ---")
        print("1. Create User")
        print("2. List Users")
        print("3. Back to Admin Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            create_user_menu()
        elif choice == '2':
            list_users_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


def create_user_menu():
    print("\n--- Create User ---")
    name = input("Enter user name: ")
    role = input("Enter user role (admin, teacher, student): ")
    user_data = {'name': name, 'role': role}

    if role == 'student':
        group_id = input("Enter student group id: ")
        user_data['group_id'] = int(group_id)

    if role in [r.value for r in Role]:  # check on valid role
        session = get_session()
        try:
            user = create_user(user_data)
            if user:
                # Получаем ID
                user_id = session.query(User).filter(User.name == name).first().id
                print(f"User created successfully with ID: {user_id}")
            else:
                print("Failed to create user")
        except Exception as e:
            print(f"Error creating user: {e}")
        finally:
            session.close()
    else:
        print(f"Invalid role: {role}")


def list_users_menu():
    print("\n--- List Users ---")
    users = get_all_users()
    if users:
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Role: {user.role}")
    else:
        print("No users found")


def manage_groups_menu():
    while True:
        print("\n--- Manage Groups ---")
        print("1. Create Group")
        print("2. List Groups")
        print("3. Back to Admin Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            create_group_menu()
        elif choice == '2':
            list_groups_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


def create_group_menu():
    print("\n--- Create Group ---")
    name = input("Enter group name: ")
    session = get_session()
    try:
        group = create_group({'name': name})
        if group:
            # Получаем ID группы через сессию
            group_id = session.query(Group).filter(Group.name == name).first().id
            print(f"Group created successfully with ID: {group_id}")
        else:
            print("Failed to create group")
    except Exception as e:
        print(f"Error creating group: {e}")
    finally:
        session.close()


def list_groups_menu():
    print("\n--- List Groups ---")
    groups = get_all_groups()
    if groups:
        for group in groups:
            print(f"ID: {group.id}, Name: {group.name}")
    else:
        print("No groups found")


def manage_subjects_menu():
    while True:
        print("\n--- Manage Subjects Menu ---")
        print("1. Create Subject")
        print("2. List Subjects")
        print("3. Back to Admin Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            create_subject_menu()
        elif choice == '2':
            list_subjects_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


def create_subject_menu():
    print("\n--- Create Subject ---")
    name = input("Enter subject name: ")
    teacher_id = input("Enter teacher ID: ")
    session = get_session()
    try:
        subject_data = {'name': name, 'teacher_id': int(teacher_id)}
        subject = create_subject(subject_data)
        if subject:
            # Получаем ID предмета
            subject_id = session.query(Subject).filter(Subject.name == name).first().id
            print(f"Subject created successfully with ID: {subject_id}")
        else:
            print("Failed to create subject")
    except Exception as e:
        print(f"Error create subject: {e}")
    finally:
        session.close()


def list_subjects_menu():
    print("\n--- List Subjects ---")
    subjects = get_all_subjects()
    if subjects:
        for subject in subjects:
            print(f"ID: {subject.id}, Name: {subject.name}, Teacher ID: {subject.teacher_id}")
    else:
        print("No subject found")


def manage_schedule_menu():
    while True:
        print("\n--- Manage Schedule Menu ---")
        print("1. Create Schedule")
        print("2. Back to Admin Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            create_schedule_menu()
        elif choice == '2':
            break
        else:
            print("Invalid choice.")


def create_schedule_menu():
    print("\n--- Create Schedule ---")
    date_str = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM): ")
    subject_id = input("Enter subject ID: ")
    group_id = input("Enter group ID: ")
    teacher_id = input("Enter teacher ID: ")

    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    schedule_data = {'date': date_obj, 'time': time, 'subject_id': int(subject_id), 'group_id': int(group_id),
                     'teacher_id': int(teacher_id)}

    session = get_session()
    try:
        schedule = create_schedule(schedule_data)
        if schedule:
            # Получаем ID расписания
            schedule_id = session.query(Schedule).filter(Schedule.date == date_obj).first().id
            print(f"Schedule created successfully with ID: {schedule_id}")
        else:
            print("Failed to create schedule")
    except Exception as e:
        print(f"Error creating schedule {e}")
    finally:
        session.close()


def manage_semesters_menu():
    while True:
        print("\n--- Manage Semesters Menu ---")
        print("1. Create Semester")
        print("2. List Semesters")
        print("3. Back to Admin Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_semester_menu()
        elif choice == '2':
            list_semesters_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


def create_semester_menu():
    print("\n--- Create Semester ---")
    name = input("Enter semester name: ")
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    semester_data = {'name': name, 'start_date': start_date, 'end_date': end_date}

    session = get_session()
    try:
        semester = create_semester(semester_data)
        if semester:
            print(f"Semester created successfully with ID: {semester.id}")
        else:
            print("Failed to create semester")
    except Exception as e:
        pass
        # print(f"Error create semester: {e}")
    finally:
        session.close()


def list_semesters_menu():
    print("\n--- List Semesters ---")
    semesters = get_all_semesters()
    if semesters:
        for semester in semesters:
            print(
                f"ID: {semester.id}, Name: {semester.name}, Start Date: {semester.start_date}, End Date: {semester.end_date}")
    else:
        print("No semesters found")


def assign_subject_to_semester_menu():
    print("\n--- Assign Subject to Semester ---")
    semester_id = input("Enter semester ID: ")
    subject_id = input("Enter subject ID: ")
    if assign_subject_to_semester(int(semester_id), int(subject_id)):
        print("Subject assigned to semester successfully.")
    else:
        print("Failed to assign subject to semester")