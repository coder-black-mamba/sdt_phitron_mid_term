# bismillahir rahmanir rahim
import random


# this is my function for getting random number for student id
def get_random_id():
    return random.randint(10000, 99999)




# The mian Student Database Class
class StudentDatabase:
    # add a class attribute named student_list
    __student_list = []
    def __init__(self):
        pass


    # defining a add_student method to insert an object of Student Class
    @classmethod
    def add_student(cls,student_obj):
        cls.__student_list.append(student_obj)

    # defining the class method for viewing all the student data
    @classmethod
    def view_all_students(cls):
        for student in cls.__student_list:
            student.view_student_info(True)
            # churi kora style
            # print(f"Student ID: {student._Student__student_id}, Name : {student._Student__name}, Department : {student._Student__department}, Enrollment Status : {student._Student__is_enrolled}")




# defining the Student Class
class Student:
    def __init__(self, student_id, name,department,is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    # method for enrolling student
    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student [ ID: {self.__student_id} , Name : {self.__name} ] is already enrolled :) ")
        else:
            self.__is_enrolled=True
            print(f"Student [ ID : {self.__student_id}, Name : {self.__name}, Department : {self.__department}, Enrolled : {self.__is_enrolled} ] Enrollment Successful 🤓🤓🤓")
            # print(f"ID : {self.__student_id}, Name : {self.__name}, Department : {self.__department}, Enrolled : {self.__is_enrolled}")

    # method for drop student
    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled=False
            print(f"Student [ ID : {self.__student_id}, Name : {self.__name} ] - Dropped Successfully 😭😭😭")
        else:
            print(f"Student [ ID: {self.__student_id} , Name : {self.__name} ] is Not Enrolled Yet :) ")


    # view student info method for viewing the student data
    def view_student_info(self ,db_style=False):
        enrollment_status="Not Enrolled"

        if self.__is_enrolled:
            enrollment_status="Enrolled"

        # for my 2 type of style
        if db_style:
            print(f"ID : {self.__student_id},Name : {self.__name},Department :{self.__department},Enrolled : {enrollment_status}")
        else:
            print(f"The ID of the student {self.__name} is: {self.__student_id} .He/She is in the DEPT of {self.__department} and currently he/she is  {enrollment_status} .")


kodu = Student(get_random_id(), "Kodu", "CSE")
jodu = Student(get_random_id(), "Jodu", "CSE")
modu = Student(get_random_id(), "Modu", "EEE")
lodu = Student(get_random_id(), "Lodu", "EEE")
sahbagi = Student(get_random_id(), "Sahbagi", "Charukola")

kodu.enroll_student()

jodu.view_student_info()
kodu.view_student_info()

kodu.drop_student()
jodu.drop_student()
modu.drop_student()

# StudentDatabase.view_all_students()