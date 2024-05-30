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
        stdnt = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.grades}\nКурсы в процессе изучения: {self.courses_in_progress}\nОконченые курсы: {self.finished_courses}"
        return stdnt

    def avg_grades(self):
        grades_list = sum(self.grades.values(), start=[])
        return round(sum(grades_list) / len(grades_list), 2)

    def __It__(self, other):
        if isinstance(other, Student):
            print('Ошибка')
            return
        return self.avg_grades() < other.avg_grades()


student_list = []
student_list.append(Student('Mihail', 'Evdokimov', 'male'))
student_list.append(Student('Aleksandr', 'Schvetsov', 'male'))
student_list.append(Student('Anastasia', 'Tagulova', 'female'))
student_list.append(Student('Polina', 'Karmanova', 'female'))

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
        lctr = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades}'
        return lctr

lecturers_list = []
lecturers_list.append(Lecturer('Steve', 'Jobs'))
lecturers_list.append(Lecturer('Faraon', 'Tutanhamon'))

lecturers_list[0].lec += ['Python', 'Git']
lecturers_list[1].lec += ['Python', 'Git']

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


