from pprint import pprint

class Subscriptable(type):
    def __getitem__(self, k):
        return self.items[k]
class Student(metaclass=Subscriptable):
    items = []
    def __init__(self, name, surname, gender, finished_courses, courses_in_progress, grades):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lection(self, lecturer, lection, rate):
        if isinstance(lecturer, Lecturer) and lection in self.courses_in_progress and lection in lecturer.courses_attached:
            if lection in lecturer.ratings:
                if 1 <= int(rate) <= 10:
                    lecturer.ratings[lection] += [rate]
                else:
                    print('введите оценку от 1 до 10')
            else:
                lecturer.ratings[lection] = [rate]
        else:
            return('Ошибка')

    def __str__(self):
        return(f" Имя:  {self.name}, \n Фамилия: {self.surname}")

    def average_grade(self):
        count_grades = 0
        sum_grades = 0
        for course_name, marks in self.grades.items():
            for mark in marks:
                sum_grades += int(mark)
            count_grades += len(marks)
        average_mark = sum_grades / count_grades
        return average_mark

    def __str__(self):
        return f' Имя: {self.name},\n Фамилия: {self.surname},\n Средняя оценка за домашние задания: {self.average_grade()},\n Курсы в процессе изучения: {", ".join(self.courses_in_progress)},\n Завершенные курсы: {", ".join(self.finished_courses)}.'

    def __gt__(self, other: 'Student'):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other: 'Student'):
        return self.average_grade() >= other.average_grade()

    def __lt__(self, other: 'Student'):
        return self.average_grade() < other.average_grade()

    def __le__(self, other: 'Student'):
        return self.average_grade() <= other.average_grade()

class Mentor:
    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer(Mentor, metaclass=Subscriptable):
    items = []

    def __init__(self, name, surname, courses_attached, ratings):
        super().__init__(name, surname, courses_attached)
        self.ratings = {}

    def average_rate(self):
        count_rates = 0
        sum_rating = 0
        for course, points in self.ratings.items():
            for point in points:
                sum_rating += int(point)
            count_rates += len(points)
        average_rating = sum_rating / count_rates
        return average_rating

    def __str__(self):
        return(f'Имя:  {self.name},\n Фамилия:  {self.surname},\n Средняя оценка за лекции: {self.average_rate()}.')

    def __gt__(self, other: 'Lecturer'):
        return self.average_rating() > other.average_rating()

    def __ge__(self, other: 'Lecturer'):
        return self.average_rating() >= other.average_rating()

    def __lt__(self, other: 'Lecturer'):
        return self.average_rating() < other.average_rating()

    def __le__(self, other: 'Lecturer'):
        return self.average_rating() <= other.average_rating()


class Reviewer(Mentor):

    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return('Ошибка')

    def __str__(self):
        return(f" Имя:  {self.name}, \n Фамилия: {self.surname}")

students_db = [Student('Peter', 'Maslov', 'male', [], [], {}),
            Student('Vasya', 'Lvova', 'female', [], [], {}),
            Student('John', 'Kazinik', 'male', [], [], {})]

students_db[0].finished_courses += ['Java Script']
students_db[1].finished_courses += ['Frontend-developer']
students_db[2].finished_courses += ['Python-developer']

students_db[0].courses_in_progress += ['Fullstack-development']
students_db[1].courses_in_progress += ['Fullstack-development']
students_db[2].courses_in_progress += ['Fullstack-development']

Reviewer1 = Reviewer('Pavel', 'Fursov', [])
Reviewer1.courses_attached += ['Fullstack-development']
Reviewer1.rate_hw(students_db[0], 'Fullstack-development', '7')
Reviewer1.rate_hw(students_db[1], 'Fullstack-development', '9')
Reviewer1.rate_hw(students_db[2], 'Fullstack-development', '8')
Reviewer1.rate_hw(students_db[0], 'Fullstack-development', '9')
Reviewer1.rate_hw(students_db[1], 'Fullstack-development', '9')
Reviewer1.rate_hw(students_db[2], 'Fullstack-development', '10')

average_grades_sum = 0
total_count = 0

for learner in students_db:
    average_grades_sum += learner.average_grade()
    total_count +=1
all_students_average_grade = average_grades_sum / total_count
print(all_students_average_grade)

lecturer1 = Lecturer('Alexandr', 'Poletaev', [], {})
lecturer1.courses_attached += ['Fullstack-development']
students_db[0].rate_lection(lecturer1, 'Fullstack-development', '10')
students_db[1].rate_lection(lecturer1, 'Fullstack-development', '9')
students_db[2].rate_lection(lecturer1, 'Fullstack-development', '10')

#for i in range(len(students_db)):
print(students_db[0])
print(Reviewer1)
print(lecturer1)