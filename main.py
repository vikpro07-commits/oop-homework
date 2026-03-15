# ==========================================================
# Netology Python course
# OOP Homework
# ==========================================================
# Исправления по замечаниям:
# 1. Классы объявлены только ОДИН раз (убрано дублирование).
# 2. Магические методы сравнения (__lt__, __eq__) возвращают
#    NotImplemented при сравнении с объектами другого типа.
# 3. Проверки типов добавлены через isinstance().
# ==========================================================


# ==========================================================
# БАЗОВЫЕ КЛАССЫ (объявляются один раз для всех заданий)
# ==========================================================

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Студент оценивает лектора
    def rate_lecture(self, lecturer, course, grade):

        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'

        if course not in self.courses_in_progress:
            return 'Ошибка'

        if course not in lecturer.courses_attached:
            return 'Ошибка'

        lecturer.grades.setdefault(course, []).append(grade)

    # Средняя оценка студента
    def average_grade(self):

        all_grades = []

        for grades in self.grades.values():
            all_grades.extend(grades)

        if not all_grades:
            return 0

        return sum(all_grades) / len(all_grades)

    # Магический метод вывода
    def __str__(self):

        avg = round(self.average_grade(), 1)

        courses = ", ".join(self.courses_in_progress)
        finished = ", ".join(self.finished_courses)

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg}\n"
            f"Курсы в процессе изучения: {courses}\n"
            f"Завершенные курсы: {finished}"
        )

    # Сравнение студентов
    def __lt__(self, other):

        if not isinstance(other, Student):
            return NotImplemented  # исправлено

        return self.average_grade() < other.average_grade()

    def __eq__(self, other):

        if not isinstance(other, Student):
            return NotImplemented  # исправлено

        return self.average_grade() == other.average_grade()


# ==========================================================
# Родительский класс Mentor
# ==========================================================

class Mentor:

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname

        self.courses_attached = []


# ==========================================================
# Класс Lecturer
# ==========================================================

class Lecturer(Mentor):

    def __init__(self, name, surname):

        super().__init__(name, surname)

        self.grades = {}

    def average_grade(self):

        all_grades = []

        for grades in self.grades.values():
            all_grades.extend(grades)

        if not all_grades:
            return 0

        return sum(all_grades) / len(all_grades)

    def __str__(self):

        avg = round(self.average_grade(), 1)

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg}"
        )

    # Сравнение лекторов
    def __lt__(self, other):

        if not isinstance(other, Lecturer):
            return NotImplemented  # исправлено

        return self.average_grade() < other.average_grade()

    def __eq__(self, other):

        if not isinstance(other, Lecturer):
            return NotImplemented  # исправлено

        return self.average_grade() == other.average_grade()


# ==========================================================
# Класс Reviewer
# ==========================================================

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):

        if not isinstance(student, Student):
            return 'Ошибка'

        if course not in self.courses_attached:
            return 'Ошибка'

        if course not in student.courses_in_progress:
            return 'Ошибка'

        student.grades.setdefault(course, []).append(grade)

    def __str__(self):

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )


# ==========================================================
# ЗАДАНИЕ 1 — Наследование
# ==========================================================

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lecturer, Mentor))  # True
print(isinstance(reviewer, Mentor))  # True

print(lecturer.courses_attached)
print(reviewer.courses_attached)


# ==========================================================
# ЗАДАНИЕ 2 — Атрибуты и взаимодействие классов
# ==========================================================

student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))
print(student.rate_lecture(lecturer, 'Java', 8))
print(student.rate_lecture(lecturer, 'C++', 8))
print(student.rate_lecture(reviewer, 'Python', 6))

print(lecturer.grades)


# ==========================================================
# ЗАДАНИЕ 3 — Полиморфизм и магические методы
# ==========================================================

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 9)

student.rate_lecture(lecturer, 'Python', 9)
student.rate_lecture(lecturer, 'Python', 10)

print(student)
print()
print(lecturer)
print()
print(reviewer)


# ==========================================================
# ЗАДАНИЕ 4 — Полевые испытания
# ==========================================================

def average_hw_grade(students, course):

    total = 0
    count = 0

    for student in students:

        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])

    if count == 0:
        return 0

    return round(total / count, 1)


def average_lecture_grade(lecturers, course):

    total = 0
    count = 0

    for lecturer in lecturers:

        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])

    if count == 0:
        return 0

    return round(total / count, 1)


# Полевые испытания

student1 = Student('Ruoy', 'Eman', 'Ж')
student2 = Student('Anna', 'Smith', 'Ж')

lecturer1 = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('John', 'Brown')

reviewer1 = Reviewer('Peter', 'Parker')
reviewer2 = Reviewer('Mary', 'Jane')

student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Python']

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']

reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 8)

student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 7)

print(student1 > student2)
print(lecturer1 == lecturer2)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print("Средняя оценка студентов по курсу Python:",
      average_hw_grade(students, 'Python'))

print("Средняя оценка лекторов по курсу Python:",
      average_lecture_grade(lecturers, 'Python'))
# ==========================================================
# Проверка функций задания №4
# ==========================================================

students = [student]
lecturers = [lecturer]

print(
    "Средняя оценка студентов по курсу Python:",
    average_hw_grade(students, 'Python')
)

print(
    "Средняя оценка лекторов по курсу Python:",
    average_lecture_grade(lecturers, 'Python')
)
