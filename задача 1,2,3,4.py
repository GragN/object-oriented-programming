class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в програмирование']
        self.courses_in_progress = []
        self.grades = {}
        self.number = 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        for i in self.grades.values():
            self.number = sum(i)
            result = self.number/len(self.grades.values())
            return result

    def __str__(self):
        res = f'имя: {self.name} \nфамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.average()} \n' \
              f'Курсы в процессе обучения: {", ".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('not a Student')
            return
        return self.average() < other.average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.number = 0

    def average(self):
        for i in self.grades.values():
            self.number = sum(i)
            result = self.number/len(self.grades.values())
            return result

    def __str__(self):
        res = f'имя: {self.name} \nфамилия: {self.surname} \nСредняя оценка за лекции: {self.average()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('not a Lecturer')
            return
        return self.average() < other.average()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'имя: {self.name} \nфамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.courses_attached += ['Python']

cool_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student.courses_in_progress += ['Python']

cool_student.rate_lecturer(best_lecturer, 'Python', 10)
cool_student.rate_lecturer(best_lecturer, 'Python', 10)
cool_student.rate_lecturer(best_lecturer, 'Python', 10)
cool_student.rate_lecturer(best_lecturer, 'Python', 9)

print(best_lecturer.grades)

new_student = Student('Bob', 'Man', 'your_gender')
new_student.courses_in_progress += ['Git']

cool_reviewer = Reviewer('Buddy', 'Some',)
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(new_student, 'Git', 5)
cool_reviewer.rate_hw(new_student, 'Git', 6)
cool_reviewer.rate_hw(new_student, 'Git', 3)
cool_reviewer.rate_hw(new_student, 'Git', 8)

print(new_student.grades)

new_lecturer = Lecturer('Buddy', 'Som')
new_lecturer.courses_attached += ['Git']

cool_student = Student('Rob', 'Man', 'your_gender')
cool_student.courses_in_progress += ['Git']

cool_student.rate_lecturer(new_lecturer, 'Git', 6)
cool_student.rate_lecturer(new_lecturer, 'Git', 2)
cool_student.rate_lecturer(new_lecturer, 'Git', 9)
cool_student.rate_lecturer(new_lecturer, 'Git', 10)

print(new_lecturer.grades)

print(cool_reviewer, '\n')
print(best_lecturer, '\n')
print(best_student, '\n')
print(cool_reviewer, '\n')
print(new_lecturer, '\n')
print(new_student, '\n')

print(best_lecturer.average() < best_student.average())
print(new_lecturer.average() > new_student.average())

def average_students_grade(course, students):
    new_list = list()
    for i in students:
        if ''.join(i.grades.keys()) == course:
            new_list.append(int(i.average()))
        else:
            pass
    #print(new_list)
    average_student_grade = sum(new_list)/len(new_list)
    print(f'Средняя оценка дз всех студентов по курсу {course} = {average_student_grade}')

def average_lecturers_grade(course, lecturer):
    new_list = list()
    for i in lecturer:
        if ''.join(i.grades.keys()) == course:
            new_list.append(int(i.average()))
        else:
            pass
    #print(new_list)
    average_student_grade = sum(new_list)/len(new_list)
    print(f'Средняя оценка за лекции всех лекторов по курсу {course} = {average_student_grade}')


average_students_grade('Python', [best_student, new_student])
average_students_grade('Git', [best_student, new_student])

average_lecturers_grade('Python', [best_lecturer, new_lecturer])
average_lecturers_grade('Git', [best_lecturer, new_lecturer])
