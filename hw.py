class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lector, lec, grade):
        if isinstance(lector, Lecturer) and lec in lector.lec:
            if lec in lector.grades:
                lector.grades[lec] += [grade]
            else:
                lector.grades[lec] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        stdnt = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.avg_grades()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nОконченые курсы: {", ".join(self.finished_courses)}"
        return stdnt

    # Средняя оценка студента по курсу
    def avg_grades(self):
        grades_list = sum(self.grades.values(), start=[])
        return round(sum(grades_list) / len(grades_list), 2)

    # Сравнение оценок студентов
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.avg_grades() < other.avg_grades()

# Списки студеннтов
student_list = []
student_list.append(Student('Mihail', 'Evdokimov', 'male'))
student_list.append(Student('Aleksandr', 'Schvetsov', 'male'))
student_list.append(Student('Anastasia', 'Tagulova', 'female'))
student_list.append(Student('Polina', 'Karmanova', 'female'))

# Закрепленные курсы за студентами
student_list[0].courses_in_progress += ['Python']
student_list[0].finished_courses += ['Java']
student_list[1].finished_courses += ['Java']
student_list[1].courses_in_progress += ['Python']
student_list[2].finished_courses += ['Python']
student_list[2].courses_in_progress += ['Java']
student_list[3].courses_in_progress += ['Python']
student_list[3].finished_courses += ['Java']

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        mnt = f'Имя: {self.name}\nФамилия: {self.surname}'
        return mnt

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.lec = []
        self.grades = {}

    def __str__(self):
        lctr = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grades_lec()}'
        return lctr

    # Сравнение оценок лекторов
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.avg_grades_lec() < other.avg_grades_lec()

    # Средняя оценка лекторов
    def avg_grades_lec(self):
        grades_list = sum(self.grades.values(), start=[])
        return round(sum(grades_list) / len(grades_list), 2)




lecturers_list = []
lecturers_list.append(Lecturer('Steve', 'Jobs'))
lecturers_list.append(Lecturer('Faraon', 'Tutanhamon'))

lecturers_list[0].lec += ['Python', 'Java']
lecturers_list[1].lec += ['Python', 'Java']

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


mentors_list = []
mentors_list.append(Reviewer('Konstantin', 'Vorobiev'))
mentors_list.append(Reviewer('Georgiy', 'Chivchyan'))

mentors_list[0].courses_attached += ['Python', 'Java']
mentors_list[1].courses_attached += ['Python', 'Java']

# Выставление оценок студентам
mentors_list[0].rate_hw(student_list[0], 'Python', 4)
mentors_list[1].rate_hw(student_list[0], 'Java', 9)
mentors_list[0].rate_hw(student_list[1], 'Python', 10)
mentors_list[1].rate_hw(student_list[1], 'Python', 7)
mentors_list[0].rate_hw(student_list[2], 'Java', 8)
mentors_list[1].rate_hw(student_list[2], 'Python', 6)
mentors_list[0].rate_hw(student_list[3], 'Java', 3)
mentors_list[1].rate_hw(student_list[3], 'Python', 7)

# Выставление оценок лекторам
student_list[0].rate_lecturer(lecturers_list[0], 'Python', 6)
student_list[0].rate_lecturer(lecturers_list[0], 'Java', 5)
student_list[1].rate_lecturer(lecturers_list[1], 'Python', 9)
student_list[1].rate_lecturer(lecturers_list[0], 'Java', 3)
student_list[2].rate_lecturer(lecturers_list[0], 'Python', 10)
student_list[2].rate_lecturer(lecturers_list[1], 'Java', 9)
student_list[3].rate_lecturer(lecturers_list[1], 'Python', 4)
student_list[3].rate_lecturer(lecturers_list[1], 'Java', 8)

# Средняя оценка всех студентов по определенному курсу
def total(student_list, course):
    all_grades = []
    for student in student_list:
        for key, value in student.grades.items():
            if key == course:
                all_grades.extend(value)
    return sum(all_grades) / len(all_grades)

# Средняя оценка всех лекторов по определенному курсу
def total(lecturers_list, course):
    all_grades = []
    for lecturer in lecturers_list:
        for key, value in lecturer.grades.items():
            if key == course:
                all_grades.extend(value)
    return sum(all_grades) / len(all_grades)


# Вывод
print(student_list[3])
print('========')
print(lecturers_list[1])
print('========')
print(mentors_list[1])
print('========')
print(total(student_list, 'Java'))
print('========')
print(total(lecturers_list, 'Python'))
print('========')
print(Lecturer.avg_grades_lec(student_list[1]))
print('========')
print(Student.avg_grades(student_list[2]))
print('========')
print(student_list[1] > student_list[3])
print('========')
print(lecturers_list[0] > lecturers_list[1])