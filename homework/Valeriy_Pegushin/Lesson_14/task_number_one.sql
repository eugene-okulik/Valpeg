INSERT INTO students (name, second_name, group_id) VALUES ('Иван', 'Иванов', 1);

INSERT INTO books (title, taken_by_student_id) VALUES ('Математический анализ', 21113), ('Основы программирования', 21113), ('Базы данных и SQL', 21113);

INSERT INTO `groups` (title, start_date, end_date) VALUES ('ИТ-101', '2024-09-01', '2028-06-30');

INSERT INTO subjects (title) VALUES ('Математический анализ'), ('Основы программирования'), ('Базы данных');

INSERT INTO lessons (title, subject_id) VALUES ('Введение в математический анализ. Пределы', 11903), ('Решение задач на вычисление пределов', 11903), ('Введение в программирование. Переменные и типы данных', 11904), ('Написание первой программы на Python', 11904), ('Реляционная модель данных. Нормальные формы', 11905), ('Создание таблиц и простые SQL-запросы', 11905);

INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 12096, 21113), (4, 12097, 21113), (5, 12098, 21113), (3, 12099, 21113), (4, 12100, 21113), (5, 12101, 21113);

SELECT * FROM marks WHERE student_id = 21113;

SELECT * FROM books WHERE taken_by_student_id = 21113;

SELECT
    s.id as student_id,
    s.name,
    s.second_name,
    g.title as group_name,
    b.title as book_title,
    sub.title as subject_title,
    l.title as lesson_title,
    m.value as mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = 21113;

