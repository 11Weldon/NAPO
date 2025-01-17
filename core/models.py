from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SqlEnum, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import Table

Base = declarative_base()


class Role(Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(SqlEnum(Role))
    # Убрали polymorphic_on
    # __mapper_args__ = {
    # "polymorphic_on": role,
    # }


class Student(User):
    __tablename__ = 'students'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")
    attendances = relationship("Attendance", back_populates="student")

    __mapper_args__ = {
        "polymorphic_identity": Role.STUDENT
    }


class Teacher(User):
    __tablename__ = 'teachers'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    subjects = relationship("Subject", back_populates="teacher")

    __mapper_args__ = {
        "polymorphic_identity": Role.TEACHER
    }


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", back_populates="group")


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")
    attendances = relationship("Attendance", back_populates="subject")
    schedule_items = relationship("Schedule", back_populates="subject")


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    value = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")


class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)  # Убрали ForeignKey
    # id = Column(Integer, ForeignKey('students.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    date = Column(DateTime, default=datetime.utcnow)
    status = Column(String)  # "present", "absent"

    student = relationship("Student", back_populates="attendances")
    subject = relationship("Subject", back_populates="attendances")


class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    time = Column(String)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    subject = relationship("Subject", back_populates="schedule_items")
    group = relationship("Group")
    teacher = relationship("Teacher")


semester_subject_association = Table(
    'semester_subject_association', Base.metadata,
    Column('semester_id', Integer, ForeignKey('semesters.id')),
    Column('subject_id', Integer, ForeignKey('subjects.id'))
)


class Semester(Base):
    __tablename__ = 'semesters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    subjects = relationship("Subject", secondary=semester_subject_association)  # corrected


class Notification(Base):
    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String)
    date = Column(DateTime, default=func.now())