# Импорт модуля для работы с MySQL
import mysql.connector as mysql
# Импорт модуля для работы с операционной системой
import os
# Импорт модуля для работы с .env файлами
import dotenv
# Импорт модуля для работы с CSV файлами
import csv

# Загрузка переменных окружения из .env файла (override=True означает перезапись существующих переменных)
dotenv.load_dotenv(override=True)

# Получение пути к текущей директории скрипта
base_path = os.path.dirname(__file__)
# Получение пути к родительской директории (на два уровня выше)
homework_path = os.path.dirname(os.path.dirname(base_path))
# Формирование полного пути к CSV файлу
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

# Инициализация пустого списка для хранения данных из CSV
csv_data = []
# Открытие CSV файла для чтения с указанием кодировки UTF-8
with open(file_path, 'r', encoding='utf-8') as file:
    # Создание объекта DictReader для чтения CSV как словарей
    csv_dict_reader = csv.DictReader(file)
    # Итерация по каждой строке в CSV файле
    for row in csv_dict_reader:
        # Добавление строки (в виде словаря) в список csv_data
        csv_data.append(dict(row))
        print(dict(row))

# Установление соединения с базой данных MySQL
db = mysql.connect(
    # Получение имени пользователя из переменных окружения
    user=os.getenv('DB_USER'),
    # Получение пароля из переменных окружения
    passwd=os.getenv('DB_PASSWD'),
    # Получение хоста из переменных окружения
    host=os.getenv('DB_HOST'),
    # Получение порта из переменных окружения и преобразование в integer
    port=int(os.getenv('DB_PORT')),
    # Получение имени базы данных из переменных окружения
    database=os.getenv('DB_DATABASE'),
)

# Создание курсора для выполнения SQL запросов (dictionary=True для возврата результатов в виде словарей)
cursor = db.cursor(dictionary=True)
# SQL запрос для выборки данных из нескольких таблиц с JOIN
query = """
SELECT s.name, s.second_name, g.title as group_title, b.title as book_title, 
       sub.title as subject_title, l.title as lesson_title, m.value as mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
"""
# Выполнение SQL запроса
cursor.execute(query)
# Получение всех результатов запроса
db_data = cursor.fetchall()

# Инициализация пустого списка для хранения записей, отсутствующих в базе данных
missing_in_db = []

# Итерация по каждой строке из CSV файла
for csv_row in csv_data:
    # Флаг для отслеживания найден ли соответствующий элемент в базе данных
    found = False
    # Итерация по каждой строке из базы данных
    for db_row in db_data:
        # Преобразование значения оценки из базы данных в строку (если значение None, то пустая строка)
        db_mark = str(db_row['mark_value']) if db_row['mark_value'] is not None else ''

        # Сравнение всех полей CSV строки с соответствующими полями из базы данных
        if (csv_row['name'] == db_row['name'] and
                csv_row['second_name'] == db_row['second_name'] and
                csv_row['group_title'] == db_row['group_title'] and
                csv_row['book_title'] == db_row['book_title'] and
                csv_row['subject_title'] == db_row['subject_title'] and
                csv_row['lesson_title'] == db_row['lesson_title'] and
                csv_row['mark_value'] == db_mark):
            # Если все поля совпадают, устанавливаем флаг found в True
            found = True
            # Прерываем внутренний цикл, так как совпадение найдено
            break

    # Если совпадение не найдено после проверки всех записей из базы данных
    if not found:
        # Добавляем CSV строку в список отсутствующих в базе данных
        missing_in_db.append(csv_row)

# Проверка есть ли отсутствующие данные в базе
if missing_in_db:
    # Вывод сообщения о наличии отсутствующих данных
    print("Данные, которые есть в CSV файле, но отсутствуют в базе данных:")
    # Итерация по всем отсутствующим записям и их вывод
    for row in missing_in_db:
        print(row)
else:
    # Вывод сообщения о полном соответствии данных
    print("Все данные из CSV файла присутствуют в базе данных!")

# Закрытие курсора (освобождение ресурсов)
cursor.close()
# Закрытие соединения с базой данных
db.close()