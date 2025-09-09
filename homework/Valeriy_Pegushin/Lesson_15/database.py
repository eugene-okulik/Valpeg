# Импортируем библиотеку для работы с MySQL
import mysql.connector as mysql

# Устанавливаем соединение с базой данных
db = mysql.connect(
    user='st-onl',  # Имя пользователя БД
    passwd='AVNS_tegPDkI5BlB2lW5eASC',  # Пароль пользователя
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',  # Хост БД
    port=25060,  # Порт для подключения
    database='st-onl'  # Название базы данных
)

# Создаем курсор для выполнения SQL-запросов
cursor = db.cursor()

# SQL-запрос для вставки нового студента
student_query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
# Данные для вставки (имя и фамилия студента)
student_values = ('Иван', 'Иванов')
# Выполняем запрос на вставку студента
cursor.execute(student_query, student_values)
# Получаем ID вставленного студента
student_id = cursor.lastrowid

# SQL-запрос для вставки нескольких книг
books_query = """INSERT INTO books (title, taken_by_student_id) 
                 VALUES (%s, %s), (%s, %s), (%s, %s)"""
# Данные для вставки книг (названия и ID студента, который взял книги)
books_values = (
    'Математический анализ', student_id,
    'Основы программирования', student_id,
    'Базы данных и SQL', student_id
)
# Выполняем запрос на вставку книг
cursor.execute(books_query, books_values)

# SQL-запрос для вставки новой группы (используем обратные кавычки "groups" - зарезервированное слово)
group_query = """INSERT INTO `groups` (title, start_date, end_date) 
                 VALUES (%s, %s, %s)"""
# Данные для вставки группы (название, дата начала и окончания)
group_values = ('ИТ-101', '2024-09-01', '2028-06-30')
# Выполняем запрос на вставку группы
cursor.execute(group_query, group_values)
# Получаем ID вставленной группы
group_id = cursor.lastrowid

# SQL-запрос для обновления данных студента (добавление его в группу)
update_query = "UPDATE students SET group_id = %s WHERE id = %s"
# Выполняем запрос на обновление (устанавливаем group_id для студента)
cursor.execute(update_query, (group_id, student_id))

# Добавляем предметы и сразу получаем их ID
cursor.execute("INSERT INTO subjects (title) VALUES ('Математический анализ')")
math_id = cursor.lastrowid

cursor.execute("INSERT INTO subjects (title) VALUES ('Основы программирования')")
prog_id = cursor.lastrowid

cursor.execute("INSERT INTO subjects (title) VALUES ('Базы данных')")
db_id = cursor.lastrowid

# Добавляем уроки для каждого предмета
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Введение в математический анализ. Пределы', %s)", (math_id,))
lesson1_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Решение задач на вычисление пределов', %s)", (math_id,))
lesson2_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Введение в программирование. Переменные и типы данных', %s)", (prog_id,))
lesson3_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Написание первой программы на Python', %s)", (prog_id,))
lesson4_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Реляционная модель данных. Нормальные формы', %s)", (db_id,))
lesson5_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Создание таблиц и простые SQL-запросы', %s)", (db_id,))
lesson6_id = cursor.lastrowid

# Добавляем оценки
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (5, %s, %s)", (lesson1_id, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (4, %s, %s)", (lesson2_id, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (5, %s, %s)", (lesson3_id, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (3, %s, %s)", (lesson4_id, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (4, %s, %s)", (lesson5_id, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (5, %s, %s)", (lesson6_id, student_id))

# Выполняем SQL-запрос к базе данных для выборки оценок студента
cursor.execute("SELECT value, lesson_id FROM marks WHERE student_id = %s", (student_id,))

# Выполняем SQL-запрос для выборки оценок студента
cursor.execute("SELECT value, lesson_id FROM marks WHERE student_id = %s", (student_id,))

# Получаем ВСЕ результаты запроса в виде списка
marks_results = cursor.fetchall()

# Перебираем все оценки из полученного списка
for value, lesson_id in marks_results:
    # Выводим информацию о каждой оценке: значение и ID урока
    print(f"Оценка {value} за урок {lesson_id}")

# Выполняем SQL-запрос для выборки книг, взятых студентом
cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (student_id,))

# Получаем ВСЕ результаты запроса в виде списка
books_results = cursor.fetchall()

# Перебираем все книги из полученного списка
for title, in books_results:
    # Выводим название каждой книги
    print(f"Книга: {title}")

# Выполняем SQL-запрос для получения полной информации о студенте
cursor.execute("""
    SELECT s.name, s.second_name, g.title, b.title, l.title, m.value
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON b.taken_by_student_id = s.id
    LEFT JOIN marks m ON m.student_id = s.id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    WHERE s.id = %s
""", (student_id,))

# Получаем ВСЕ результаты запроса в виде списка
results = cursor.fetchall()

# Перебираем все строки из полученного списка результатов
for name, second_name, group, book, lesson, mark in results:
    # Выводим основную информацию о студенте: имя, фамилия и группа
    print(f"{name} {second_name} - {group}")

    # Если книга существует (не None), выводим информацию о книге
    if book:
        print(f"Книга: {book}")

    # Если оценка существует (не None), выводим информацию об оценке и уроке
    if mark:
        print(f"Оценка {mark} за {lesson}")
# Фиксируем все изменения в базе данных
db.commit()

# Закрываем курсор
cursor.close()
# Закрываем соединение с базой данных
db.close()