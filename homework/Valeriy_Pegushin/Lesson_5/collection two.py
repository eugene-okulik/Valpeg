person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)

result_operation_one = 'результат операции: 42'
result_operation_two = 'результат операции: 514'
result_work = 'результат работы программы: 9'

# Находим индекс двоеточия
index_colon_one = result_operation_one.index(':')
index_colon_two = result_operation_two.index(':')
index_colon_three= result_work.index(':')

# Преобразуем срез после ": " в число и прибавляем к нему 10
number_one = int(result_operation_one[index_colon_one + 2:]) + 10
number_two = int(result_operation_two[index_colon_two + 2:]) + 10
number_three = int(result_work[index_colon_three + 2:]) + 10

print(number_one, number_two, number_three)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# ', '.join(students) объединяет список студентов через запятую с пробелом
# ', '.join(subjects) объединяет список предметов через запятую с пробелом
# f-строка (форматированная строка) подставляет эти объединённые списки в нужные места шаблона
txt = f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}"

print(txt)
