import statistics
Mass_grade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def format_marks(self):
        format_str = f"Оценки за курсы студента: {'; '.join(k + ': ' + ', '.join(map(str, z)) for k, z in self.grades.items())}"
        return format_str

    def rate_lec(self, lecturer, course, grade):
        if grade in Mass_grade:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                    and (course in self.courses_in_progress or course in self.finished_courses):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Курс не найден'
        else:
            return 'Оценка вне диапозона'
        return 'Оценка выставлена'

    def __str__(self):
        str_to_return = f"Имя: {self.name} " + \
                        f"\nФамилия: {self.surname} " + \
                        f"\nСредняя оценка за домашние задания: {str(self.average_rating())} " + \
                        f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} " + \
                        f"\nЗавершенные курсы: {', '.join(self.finished_courses)} "
        return str_to_return

    def average_rating(self):
        #sum = 0
        #count = 0
        try:
            average_rat = round(sum([statistics.mean(grades) for grades in self.grades.values()]) / len(self.grades), 1)
        except ZeroDivisionError:
            average_rat = 0
        return average_rat

    def __class_membership_check(self, other):
        if not isinstance(other, Student):
            print("Студентов можно сравнивать только с студентами")
            return False
        return True

    def __eq__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() == other.average_rating()

    def __ne__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() != other.average_rating()

    def __lt__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() < other.average_rating()

    def __le__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() <= other.average_rating()

    def __gt__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() > other.average_rating()

    def __ge__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() >= other.average_rating()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def format_marks(self):
        format_str = f"Оценки за курсы лектора: {'; '.join(k + ': ' + ', '.join(map(str, z)) for k, z in self.grades.items())}"
        return format_str

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {str(self.average_rating())}"

    def average_rating(self):
        try:
            average_rat_ = round(sum([statistics.mean(grades) for grades in self.grades.values()]) / len(self.grades), 1)
        except ZeroDivisionError:
            average_rat_ = 0
        return average_rat_

    def __class_membership_check(self, other):
        if not isinstance(other, Student):
            print("Студентов можно сравнивать только с студентами")
            return False
        return True

    def __eq__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() == other.average_rating()

    def __ne__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() != other.average_rating()

    def __lt__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() < other.average_rating()

    def __le__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() <= other.average_rating()

    def __gt__(self, other):
        if self.__class_membership_check(other):
            return self.average_rating() > other.average_rating()

    def __ge__(self, other):
        if self.__class_membership_check(other):
            return self.averagaverage_ratinge_rat() >= other.average_rating()



class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if grade in Mass_grade:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка проверки курса'
        else:
            return 'Оценка вне диапозона'
            return "Успешно оценено"

    def __str__(self):
        return "Имя: " + self.name + "\nФамилия: " + self.surname

def avg_list(list_person, course):
        avg_rate = 0
        sum = 0
        count = 0
        for item in list_person:
            if item.grades.get(course, 0) != 0:
                sum += statistics.mean(item.grades.get(course))
                count += 1
        try:
            avg_rate = round((sum / count), 1)
        except ZeroDivisionError:
            avg_rate = 'Error'
        return avg_rate

if __name__ == '__main__':
    list_Students = []
    list_Reviewer = []
    list_Lecturer = []

    best_student1 = Student('Pol', 'Smith', 'm')
    best_student1.courses_in_progress += ['Python']
    best_student1.courses_in_progress += ['SQL']
    best_student1.finished_courses += ['SSH']
    list_Students.append(best_student1)

    best_student2 = Student('Bradley', 'Pit', 'm')
    best_student2.courses_in_progress += ['Git']
    best_student2.courses_in_progress += ['Python']
    list_Students.append(best_student2)

    cool_reviewer1 = Reviewer('Leonardo', 'DiCaprio')
    cool_reviewer1.courses_attached += ['Python']
    cool_reviewer1.courses_attached += ['Math']
    list_Reviewer.append(cool_reviewer1)

    cool_reviewer2 = Reviewer('Jensen', 'Ackles')
    cool_reviewer2.courses_attached += ['Python']
    cool_reviewer2.courses_attached += ['Git']
    cool_reviewer2.courses_attached += ['SQL']
    cool_reviewer2.courses_attached += ['SSH']
    list_Reviewer.append(cool_reviewer2)

    cool_lecturer1 = Lecturer('Johnny', 'Depp')
    cool_lecturer1.courses_attached += ['Python']
    cool_lecturer1.courses_attached += ['Git']
    list_Lecturer.append(cool_lecturer1)

    cool_lecturer2 = Lecturer('Robert', 'Downey')
    cool_lecturer2.courses_attached += ['Python']
    cool_lecturer2.courses_attached += ['SQL']
    cool_lecturer2.courses_attached += ['SSH']
    list_Lecturer.append(cool_lecturer2)

    print("\nПроверка выставления оценок")

    print("\n[-] Поставим оценку 10 ментором (python) за домашку студенту (python): ")
    report = cool_reviewer1.rate_hw(best_student1, 'Python', 10)
    print(report)
    print(best_student1)
    print(best_student1.format_marks())

    print("\n[-] Поставим оценку 5 ментором (python) за домашку студенту (python): ")
    report = cool_reviewer1.rate_hw(best_student1, 'Python', 5)
    print(report)
    print(best_student1)
    print(best_student1.format_marks())

    print("\n[-] Поставим оценку 12 ментором (python) за домашку студенту (python): ")
    report = cool_reviewer1.rate_hw(best_student1, 'Python', 12)
    print(report)
    print(best_student1)
    print(best_student1.format_marks())

    print("\n[-] Поставим оценку 5 ментором (не Git) за домашку студенту (Git): ")
    report = cool_reviewer1.rate_hw(best_student2, 'Git', 5)
    print(report)
    print(best_student2)
    print(best_student2.format_marks())

    print("\n[-] Поставим оценку 5 ментором (SSH) за домашку студенту (оконченный SSH): ")
    report = cool_reviewer2.rate_hw(best_student1, 'SSH', 5)
    print(report)
    print(best_student1)
    print(best_student1.format_marks())

    print("\n[-] Поставим оценку 3 ментором (Git) за домашку студенту (не Git): ")
    report = cool_reviewer2.rate_hw(best_student1, 'Git', 3)
    print(report)
    print(best_student1)
    print(best_student1.format_marks())

    print("\nTесты к выставлению оценок студентами лекторам:")

    print("\n[-] Поставим оценку 10(+) студентом (python) лектору (python): ")
    report = best_student1.rate_lec(cool_lecturer1, 'Python', 10)
    print(report)
    print(cool_lecturer1)
    print(cool_lecturer1.format_marks())

    print("\n[-] Поставим оценку -8 студентом (python) лектору (python): ")
    report = best_student1.rate_lec(cool_lecturer1, 'Python', -8)
    print(report)
    print(cool_lecturer1)
    print(cool_lecturer1.format_marks())

    print("\n[-] Поставим оценку 5 студентом (SQL) лектору (не SQL): ")
    report = best_student1.rate_lec(cool_lecturer1, 'SQL', 5)
    print(report)
    print(cool_lecturer1)
    print(cool_lecturer1.format_marks())

    print("\n[-] Поставим оценку 2 студентом (не SQL) лектору (SQL): ")
    report = best_student2.rate_lec(cool_lecturer2, 'SQL', 2)
    print(report)
    print(cool_lecturer2)
    print(cool_lecturer2.format_marks())

    print("\n[-] Поставим оценку 7 студентом (закончивший SSH) лектору (SSH): ")
    report = best_student1.rate_lec(cool_lecturer2, 'SSH', 7)
    print(report)
    print(cool_lecturer2)
    print(cool_lecturer2.format_marks())

    print("\nСравнение студентов 1 и 2: ")
    print(" == : ", best_student1 == best_student2)
    print(" != : ", best_student1 != best_student2)
    print(" < : ", best_student1 < best_student2)
    print(" <= : ", best_student1 <= best_student2)
    print(" > : ", best_student1 > best_student2)
    print(" >= : ", best_student1 >= best_student2)
    print(best_student1)
    print(best_student2)

    print("\nПопробуем сравнить студента с лектором: ")
    print(" > : ", best_student1 > cool_lecturer2)

    print("\nСравнение лекторов 1 и 2: ")
    print(" == : ", cool_lecturer1 == cool_lecturer2)
    print(" != : ", cool_lecturer1 != cool_lecturer2)
    print(" < : ", cool_lecturer1 < cool_lecturer2)
    print(" <= : ", cool_lecturer1 <= cool_lecturer2)
    print(" > : ", cool_lecturer1 > cool_lecturer2)
    print(" >= : ", cool_lecturer1 >= cool_lecturer2)
    print(cool_lecturer1)
    print(cool_lecturer2)

    print("\nПопробуем сравнить лектора с студентом: ")
    print(" == : ", cool_lecturer2 == best_student1)

    cool_reviewer1.rate_hw(best_student2, 'Python', 5)
    print(f"\nСредняя оценка среди студентов по курсу Python: {avg_list(list_Students, 'Python')}")
    print(best_student1.format_marks())
    print(best_student2.format_marks())

    print(f"\nСредняя оценка среди лекторов по курсу Python: {avg_list(list_Lecturer, 'Python')}")
    print(cool_lecturer1.format_marks())
    print(cool_lecturer2.format_marks())