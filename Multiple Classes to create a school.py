class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
class Teacher:
    def __init__(self, name, course):
        self.name = name
        self.course = course
class School:
    def __init__(self, name, teachers, students, courses):
        self.name = name
        self.teachers = teachers
        self.students = students
        self.courses = courses
    def get_students(self):
        for student in self.students:
            print(student.name, student.id)
        
school_name = "Green"
ds_course = Course("DS", "Einstein")
algo_course = Course("Algorithm", "Edison")
teacher_1 = Teacher('Einstein', ds_course)
teacher_2 = Teacher('Edison', algo_course)
student_1 = Student('Tanvir', 22, 90)
student_2 = Student('Shiblu', 23, 91)

students = [student_1, student_2]
teachers = [teacher_1, teacher_2]
courses = [ds_course, algo_course]

my_school = School(school_name, teachers, students, courses)
my_school.get_students()
        