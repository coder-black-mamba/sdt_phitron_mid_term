# bismillahir rahmanir rahim


# The mian Student Database Class
class StudentDatabase:
    # add a class attribute named student_list
    __student_list = []
    def __init__(self):
        pass


    # defininng a add_student method to insert an object of Student Class
    def add_student(self, student_obj):
        if type(student_obj) == Student:
            # have to have test between those
            # StudentDatabase.student_list.append(student_obj)
            self.__student_list.append(student_obj)
        else:
            print("Please Use The Instance Of `Student` Class Only")


# defining the Student Class
class Student:
    def __init__(self, student_id, name,department,is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

