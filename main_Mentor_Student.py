class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_grade(self, name, grades: 'Student'):
        count_grades = 0
        sum_grades = 0
        for mark in self.grades:
            sum_grades += self.grades[mark]
            count_grades += 1
            average_grade = sum_grades / count_grades
        return average_grade

    def best_student(self, name, surname, average_grade):
        student_max_grade = 0
        for learner in Student.average_grade:
            if Student.average_grade[learner] > student_max_grade:
                student_max_grade = Student.average_grade[learner]
                best_student = Student[learner]
        return student_max_grade, best_student

    def rate_lection(self, lecturer, course, lection, rate):
        if isinstance(lecturer, Lecturer) and lection in self.courses_in_progress and lection in Lecturer.courses_attached:
            if lection in lecturer.ratings:
                if 1 <= rate <= 10:
                    lecturer.ratings[lection] += [rate]
                else:
                    print('введите оценку от 1 до 10')
            else:
                lecturer.ratings[lection] = [rate]
        else:
            return 'Ошибка'

    def __str__(self, name, surname, grades, courses_in_progress, finished_courses):
        a = 0
        s_grades = 0
        for j in self.grades:
            s_grades += self.grades[j]
            a += 1
            average_grade = s_grades / a
        print(f"Имя: , {self.name},\n Фамилия: , {self.surname},\n Средняя оценка за домашние задания: {self.average_grade()},\n Курсы в процессе изучения: , {self.courses_in_progress},\n Завершенные курсы: , {self.finished_courses}")

    def __gt__(self, other: 'Student'):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other: 'Student'):
        return self.average_grade() >= other.average_grade()

    def __lt__(self, other: 'Student'):
        return self.average_grade() < other.average_grade()

    def __le__(self, other: 'Student'):
        return self.average_grade() <= other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, metaclass=Subscriptable):
    items = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lection = []
        self.ratings = {}

    def average_rate(self, ratings):
        count_rates = 0
        sum_rating = 0

        for point in self.ratings:
            sum_rating += self.ratings[point]
            count_rates += 1
            average_rating = sum_rating / count_rates
            return average_rating

    def __str__(self, name, surname, average_rating):
        print(f"Имя: ', {self.name}, \n Фамилия: , {self.surname}, \n Средняя оценка за лекции: {self.average_rating()}")

    def best_lecturer(self, average_rating):
        keep_rate = 0
        for teacher in Lecturer.average_rating:
            if Lecturer.average_rating[teacher] > keep_rate:
                keep_rate = Lecturer.average_rating[teacher]
                best_lecturer = Lecturer.surname[teacher]
        return keep_rate, best_lecturer

    def __gt__(self, other: 'Lecturer'):
        return self.average_rating() > other.average_rating()

    def __ge__(self, other: 'Lecturer'):
        return self.average_rating() >= other.average_rating()

    def __lt__(self, other: 'Lecturer'):
        return self.average_rating() < other.average_rating()

    def __le__(self, other: 'Lecturer'):
        return self.average_rating() <= other.average_rating()


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self, name, surname):
        print(f"Имя: ', {self.name}, \n Фамилия: , {self.surname}")


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
