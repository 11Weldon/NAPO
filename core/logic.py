from datetime import datetime
from core.db import get_session
from core.models import Student, Teacher, Group, Subject, Grade, Attendance, Schedule, Semester, Role, User
from core.notifications import NotificationManager

notification_manager = NotificationManager()


def create_user(user_data):
    session = get_session()
    try:
        user_role = user_data.get('role')
        if user_role == 'student':
            user = Student(name=user_data['name'], group_id=user_data['group_id'], role=Role.STUDENT)  # Set role
        elif user_role == 'teacher':
            user = Teacher(name=user_data['name'], role=Role.TEACHER)  # Set role
        elif user_role == 'admin':
            user = User(name=user_data['name'], role=Role.ADMIN)
        else:
            print(f"Invalid role: {user_role}")
            return None
        session.add(user)
        session.commit()
        return user
    except Exception as e:
        session.rollback()
        print(f"Error creating user: {e}")
        return None
    finally:
        session.close()


def get_user(user_id):
    session = get_session()
    try:
        user = session.query(User).get(user_id)
        return user
    except Exception as e:
        print(f"Error getting user: {e}")
        return None
    finally:
        session.close()


def get_all_users():
    session = get_session()
    try:
        users = session.query(User).all()
        return users
    except Exception as e:
        print(f"Error getting all users: {e}")
        return None
    finally:
        session.close()


def create_group(group_data):
    session = get_session()
    try:
        group = Group(name=group_data['name'])
        session.add(group)
        session.commit()
        return group
    except Exception as e:
        session.rollback()
        print(f"Error creating group: {e}")
        return None
    finally:
        session.close()


def get_all_groups():
    session = get_session()
    try:
        groups = session.query(Group).all()
        return groups
    except Exception as e:
        print(f"Error getting all groups: {e}")
        return None
    finally:
        session.close()


def get_group(group_id):
    session = get_session()
    try:
        group = session.query(Group).filter(Group.id == group_id).first()
        return group
    except Exception as e:
        print(f"Error getting group: {e}")
        return None
    finally:
        session.close()


def create_subject(subject_data):
    session = get_session()
    try:
        teacher_id = subject_data.get('teacher_id')
        subject = Subject(name=subject_data['name'], teacher_id=teacher_id)
        session.add(subject)
        session.commit()
        return subject
    except Exception as e:
        session.rollback()
        print(f"Error creating subject: {e}")
        return None
    finally:
        session.close()


def get_subject(subject_id):
    session = get_session()
    try:
        subject = session.query(Subject).filter(Subject.id == subject_id).first()
        return subject
    except Exception as e:
        print(f"Error getting subject: {e}")
        return None
    finally:
        session.close()


def get_all_subjects():
    session = get_session()
    try:
        subjects = session.query(Subject).all()
        return subjects
    except Exception as e:
        print(f"Error getting all subjects: {e}")
        return None
    finally:
        session.close()


def add_grade(grade_data):
    session = get_session()
    try:
        grade = Grade(student_id=grade_data['student_id'], subject_id=grade_data['subject_id'],
                      value=grade_data['value'], date=datetime.now())
        session.add(grade)
        session.commit()
        notification_manager.create_notification(user_id=grade_data['student_id'],
                                                 message=f'You have a new grade: {grade_data["value"]} for the subject: {get_subject(grade_data["subject_id"]).name}')
        return grade
    except Exception as e:
        session.rollback()
        print(f"Error adding grade: {e}")
        return None
    finally:
        session.close()


def get_student_grades(student_id):
    session = get_session()
    try:
        grades = session.query(Grade).filter_by(student_id=student_id).all()
        return grades
    except Exception as e:
        print(f"Error getting student grades: {e}")
        return []
    finally:
        session.close()


def add_attendance(attendance_data):
    session = get_session()
    try:
        attendance = Attendance(student_id=attendance_data['student_id'], subject_id=attendance_data['subject_id'],
                                date=datetime.now(), status=attendance_data['status'])
        session.add(attendance)
        session.commit()
        return attendance
    except Exception as e:
        session.rollback()
        print(f"Error adding attendance: {e}")
        return None
    finally:
        session.close()


def get_student_attendance(student_id):
    session = get_session()
    try:
        attendance = session.query(Attendance).filter_by(student_id=student_id).all()
        return attendance
    except Exception as e:
        print(f"Error getting student attendance: {e}")
        return []
    finally:
        session.close()


def create_schedule(schedule_data):
    session = get_session()
    try:
        schedule = Schedule(date=schedule_data['date'], time=schedule_data['time'],
                            subject_id=schedule_data['subject_id'], group_id=schedule_data['group_id'],
                            teacher_id=schedule_data['teacher_id'])
        session.add(schedule)
        session.commit()
        return schedule
    except Exception as e:
        session.rollback()
        print(f"Error creating schedule: {e}")
        return None
    finally:
        session.close()


def get_student_schedule(student_id):
    session = get_session()
    try:
        student = session.query(Student).get(student_id)
        if student:
            schedule = session.query(Schedule).filter(Schedule.group_id == student.group_id).all()
            return schedule
        else:
            print(f"Student not found id: {student_id}")
            return []
    except Exception as e:
        print(f"Error get student schedule: {e}")
        return []
    finally:
        session.close()


def get_teacher_schedule(teacher_id):
    session = get_session()
    try:
        schedule = session.query(Schedule).filter(Schedule.teacher_id == teacher_id).all()
        return schedule
    except Exception as e:
        print(f"Error get teacher schedule: {e}")
        return []
    finally:
        session.close()


def create_semester(semester_data):
    session = get_session()
    try:
        semester = Semester(name=semester_data['name'], start_date=semester_data['start_date'],
                            end_date=semester_data['end_date'])
        session.add(semester)
        session.commit()
        return semester
    except Exception as e:
        session.rollback()
        print(f"Error creating semester: {e}")
        return None
    finally:
        session.close()


def get_all_semesters():
    session = get_session()
    try:
        semesters = session.query(Semester).all()
        return semesters
    except Exception as e:
        print(f"Error getting all semesters: {e}")
        return []
    finally:
        session.close()


def assign_subject_to_semester(semester_id, subject_id):
    session = get_session()
    try:
        semester = session.query(Semester).get(semester_id)
        subject = session.query(Subject).get(subject_id)

        if semester and subject:
            semester.subjects.append(subject)
            session.commit()
            return True
        else:
            print(f"Semester or Subject not found")
            return False
    except Exception as e:
        session.rollback()
        print(f"Error assigning subject to semester: {e}")
        return False
    finally:
        session.close()


def get_teacher_report(teacher_id, subject_id):
    session = get_session()
    try:
        grades = session.query(Grade).filter(Grade.subject_id == subject_id).all()
        if grades:
            return grades
        else:
            print("Grades not found for this subject")
            return None
    except Exception as e:
        print(f"Error get teacher report: {e}")
        return None
    finally:
        session.close()
