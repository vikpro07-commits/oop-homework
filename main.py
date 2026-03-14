# Netology Python course
# OOP homework
# Inheritance, polymorphism, magic methods
# =========================
# Задание 1. Наследование
# =========================
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and \
           course in self.courses_attached and \
           course in student.courses_in_progress:

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

        else:
            return 'Ошибка'


# Проверка работы

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)


# Проверка наследования

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lecturer, Mentor))   # True
print(isinstance(reviewer, Mentor))   # True

print(lecturer.courses_attached)      # []
print(reviewer.courses_attached)      # []

# =========================
# Задание № 2. Атрибуты и взаимодействие классов
# =========================
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}

# =========================
# Задание № 3. Полиморфизм и магические методы
# =========================
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

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

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg = round(self.average_grade(), 1)
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg}"
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )


# ===== Проверка работы =====

student = Student('Ruoy', 'Eman', 'Ж')
student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python']

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 9)

student.rate_lecture(lecturer, 'Python', 9)
student.rate_lecture(lecturer, 'Python', 10)

print(student)
print()
print(lecturer)
print()
print(reviewer)

# =========================
# Задание № 3. Полиморфизм и магические методы
# =========================

# =====================================
# Класс Student
# =====================================

class Student:
    def __init__(self, name, surname, gender):
        # Основная информация о студенте
        self.name = name
        self.surname = surname
        self.gender = gender

        # Курсы
        self.finished_courses = []        # завершенные курсы
        self.courses_in_progress = []     # курсы в процессе

        # Оценки за домашние задания
        self.grades = {}

    # Метод для выставления оценки лектору
    def rate_lecture(self, lecturer, course, grade):

        # Проверяем:
        # 1. lecturer является объектом Lecturer
        # 2. курс есть у студента
        # 3. курс закреплен за лектором
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    # Подсчет средней оценки студента
    def average_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)

        if len(all_grades) == 0:
            return 0

        return sum(all_grades) / len(all_grades)

    # Красивый вывод информации о студенте
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

    # Сравнение студентов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() == other.average_grade()


# =====================================
# Родительский класс Mentor
# =====================================

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

        # список курсов, за которые отвечает преподаватель
        self.courses_attached = []


# =====================================
# Класс Lecturer (лектор)
# =====================================

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

        # оценки за лекции
        self.grades = {}

    # подсчет средней оценки лектора
    def average_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)

        if len(all_grades) == 0:
            return 0

        return sum(all_grades) / len(all_grades)

    # вывод информации о лекторе
    def __str__(self):
        avg = round(self.average_grade(), 1)

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg}"
        )

    # сравнение лекторов
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() == other.average_grade()


# =====================================
# Класс Reviewer (проверяющий)
# =====================================

class Reviewer(Mentor):

    # выставление оценок студентам
    def rate_hw(self, student, course, grade):

        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            student.grades.setdefault(course, []).append(grade)

        else:
            return 'Ошибка'

    # вывод информации о проверяющем
    def __str__(self):

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )


# =====================================
# Функция средней оценки студентов по курсу
# =====================================

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


# =====================================
# Функция средней оценки лекторов по курсу
# =====================================

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


# =====================================
# Полевые испытания
# =====================================

# создаем студентов
student1 = Student('Ruoy', 'Eman', 'Ж')
student2 = Student('Anna', 'Smith', 'Ж')

# создаем лекторов
lecturer1 = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('John', 'Brown')

# создаем проверяющих
reviewer1 = Reviewer('Peter', 'Parker')
reviewer2 = Reviewer('Mary', 'Jane')

# назначаем курсы
student1.courses_in_progress += ['Python', 'Git']
student2.courses_in_progress += ['Python']

student1.finished_courses += ['Введение в программирование']

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']

reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']

# проверяющие выставляют оценки студентам
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)

reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 7)

# студенты оценивают лекции
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Python', 10)

student2.rate_lecture(lecturer2, 'Python', 8)
student2.rate_lecture(lecturer2, 'Python', 9)

# проверяем __str__
print(student1)
print()
print(lecturer1)
print()
print(reviewer1)

# проверяем сравнение
print(student1 > student2)
print(lecturer1 == lecturer2)

# проверяем функции средней оценки
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print("Средняя оценка студентов по курсу Python:",
      average_hw_grade(students, 'Python'))

print("Средняя оценка лекторов по курсу Python:",
      average_lecture_grade(lecturers, 'Python'))
