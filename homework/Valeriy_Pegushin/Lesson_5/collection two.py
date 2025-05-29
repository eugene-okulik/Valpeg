person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

print (name, last_name, city, phone, country)

result_operation_one = 'результат операции: 42'
result_operation_two = 'результат операции: 514'
result_work = 'результат работы программы: 9'

# Разбиваем строку на список, берём последний элемент, преобразуем в число и прибавляем к каждому  числу 10
number_onne = int(result_operation_one.split()[-1]) + 10
number_two = int(result_operation_two.split()[-1]) + 10
number_three = int(result_work.split()[-1]) + 10

# print(number_onne)
# print(number_two)
# print(number_three)
print(number_onne, number_two, number_three)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# ', '.join(students) объединяет список студентов через запятую с пробелом
# ', '.join(subjects) объединяет список предметов через запятую с пробелом
# f-строка (форматированная строка) подставляет эти объединённые списки в нужные места шаблона
txt = f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}"

print(txt)
