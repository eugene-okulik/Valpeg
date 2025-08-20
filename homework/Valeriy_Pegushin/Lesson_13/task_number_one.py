# Импортируем модуль os для работы с операционной системой (например, путями к файлам)
import os
# Импортируем модуль re для работы с регулярными выражениями (поиск дат в тексте)
import re
# Импортируем из модуля datetime необходимые классы для работы с датами и временем
from datetime import datetime, timedelta

# Получаем абсолютный путь к директории, где находится текущий исполняемый файл
base_path = os.path.dirname(__file__)
# Поднимаемся на два уровня вверх в структуре директорий (от текущего файла)
homework_path = os.path.dirname(os.path.dirname(base_path))
# Формируем полный путь к файлу data.txt, который находится в поддиректориях
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

# Выводим заголовок перед отображением содержимого файла
print("Содержимое файла:")
# Открываем файл для чтения с указанием кодировки UTF-8
with open(file_path, 'r', encoding='utf-8') as file:
    # Читаем файл построчно
    for line in file:
        # Удаляем лишние пробелы и переносы строк в начале и конце каждой строки
        print(line.strip())

# Выводим заголовок перед обработкой дат
print("\nОбработка дат:")

# Снова открываем файл для чтения (так как предыдущий with его уже закрыл)
with open(file_path, 'r', encoding='utf-8') as file:
    # Инициализируем счетчик строк
    line_number = 0
    # Читаем файл построчно
    for line in file:
        # Удаляем лишние пробелы и переносы строк
        line = line.strip()
        # Увеличиваем счетчик строк на 1
        line_number += 1

        # Если строка пустая, пропускаем ее
        if not line:
            continue

        # Ищем в строке дату в формате ГГГГ-ММ-ДД с помощью регулярного выражения
        date_match = re.search(r'\d{4}-\d{2}-\d{2}', line)
        # Если дата найдена и это одна из первых трех строк
        if date_match and line_number <= 3:
            # Извлекаем найденную дату (текстовый формат)
            date_str = date_match.group()
            # Преобразуем текстовую дату в объект datetime.date
            date = datetime.strptime(date_str, '%Y-%m-%d').date()

            # Обрабатываем первую строку
            if line_number == 1:
                # Добавляем к дате 7 дней (неделю)
                new_date = date + timedelta(days=7)
                # Выводим результат
                print(f"Строка {line_number}: Дата через неделю — {new_date}")
            # Обрабатываем вторую строку
            elif line_number == 2:
                # Получаем название дня недели (например, "Monday")
                weekday = date.strftime('%A')
                # Выводим результат
                print(f"Строка {line_number}: Это {weekday}")
            # Обрабатываем третью строку
            elif line_number == 3:
                # Получаем текущую дату
                today = datetime.now().date()
                # Вычисляем разницу между текущей датой и датой из файла
                delta = today - date
                # Выводим количество дней разницы
                print(f"Строка {line_number}: Эта дата была {delta.days} дней назад")
