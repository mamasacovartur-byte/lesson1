# class Book:
#     def __init__(self, title, author, year, pages):
#         self.title = title #название
#         self.author = author #автор
#         self.year = year #год
#         self.pages = pages #страница
#
#     def info(self):
#         print(f'название книги {self.title},',f'афтор книги {self.author},', f'создано в {self.year},', f'страница {self.pages}')
#
# book_one = Book('война и мир','Л.Т','1978','189')
# book_two = Book('крвсное яблоко','Ч.А','1997','120')
# book_free = Book('девять объезян','М.Р','1980','489')
# book_for = Book('белый пороход','Ч.А','1906','236')
#
# print(book_one.title , book_one.author , book_one.year , book_one.pages)
# print(book_two.title , book_two.author , book_two.year , book_two.pages)
# print(book_free.title , book_free.author , book_free.year , book_free.pages)
# print(book_for.title , book_for.author , book_for.year , book_for.pages)
#
# book_one.info()
# book_two.info()
# book_free.info()
# book_for.info()
# 3. Класс Student
#
# Создать файл students.py.
#
# Создать класс Student
#
# Атрибуты: name, age, course, grades (список оценок)
#
# Метод average_grade() возвращает средний балл
#
# Метод introduce() рассказывает о студенте
#
# Создать пару студентов и вывести их средние оценки.
#
# 4. Класс Animal
#
# Создать файл animals.py.
#
# Создать класс Animal
#
# Атрибуты: species, name, age
#
# Метод speak() выводит звук:
# Например: "Кот Барсик говорит: мяу!"
#
# Создать объекты разных животных.
#
# 5. Класс Movie
#
# Создать файл movies.py.
#
# Создать класс Movie
#
# Атрибуты: title, director, year, genre
#
# Метод describe() выводит описание фильма
#
# Создать 3 фильма и вывести их атрибуты.
#
# 6. Класс Employee
#
# Создать файл employee.py.
#
# Создать класс Employee
#
# Атрибуты: name, position, salary
#
# Метод info() выводит:
# "Имя: Анна, должность: менеджер, зарплата: 70000"
#
# Метод increase_salary(percent) увеличивает зарплату на заданный процент
#
# Создать несколько сотрудников и поднять одному зарплату.
#
# 7. Класс Country
#
# Создать файл countries.py.
#
# Создать класс Country
#
# Атрибуты: name, population, continent, capital
#
# Метод describe() выводит сводную информацию
#
# Создать 2–3 страны.#
# 3. Класс Student

 #Создать файл students.py.

#  Создать класс Student
#
# Атрибуты: name, age, course, grades (список оценок)
#
# Метод average_grade() возвращает средний балл
#
# Метод introduce() рассказывает о студенте
# #
# Создать пару студентов и вывести их средние оценки.#
# class Student:
#     def __init__(self, name, age, course, grades):
#         self.name = name  # имя студента
#         self.age = age  # возраст
#         self.course = course  # курс обучения
#         self.grades = grades  # список оценок
#
#     def average_grade(self):
#         """Возвращает средний балл студента"""
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
#
#     def introduce(self):
#         """Выводит информацию о студенте"""
#         print(f"Меня зовут {self.name}, мне {self.age} лет, "
#               f"я учусь на {self.course} курсе. "
#               f"Мой средний балл: {self.average_grade():.2f}")
#
#
# # Создание объектов студентов
# student_one = Student("Алибек", 18, 1, [5, 4, 5, 3, 4])
# student_two = Student("Айдана", 20, 2, [4, 4, 5, 5, 5])
#
# # Вывод средних оценок
# print("Средний балл студента 1:", student_one.average_grade())
# print("Средний балл студента 2:", student_two.average_grade())
#
# # Представление студентов
# student_one.introduce()
# student_two.introduce()