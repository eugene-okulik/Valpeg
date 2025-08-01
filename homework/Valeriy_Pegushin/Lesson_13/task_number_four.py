# Импорт модуля для работы с операционной системой (файлы, пути и т. д.)
import os
# Импорт классов datetime и timedelta из модуля datetime для работы с датами и временем
from datetime import datetime, timedelta


# Получение абсолютного пути к директории текущего скрипта (где выполняется код)
base_path = os.path.dirname(__file__)
# Получение пути к родительской директории (на уровень выше, чем base_path)
homework_path = os.path.dirname(os.path.dirname(base_path))
# Формирование полного пути к файлу data.txt, который находится в папке eugene_okulik/hw_13/
eugene_okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


# Открытие файла data.txt в режиме чтения ('r' по умолчанию)
with open(eugene_okulik_file_path) as eugene_okulik_file:
    # Чтение всего содержимого файла и вывод его в консоль
    print(eugene_okulik_file.read())


# Исходная дата в виде строки
date_str = "2023-11-27 20:34:13.212967"

# Преобразуем строку в объект datetime
original_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

# Добавляем неделю (7 дней)
new_date = original_date + timedelta(days=7)

# Выводим результат в том же формате
print(new_date.strftime("%Y-%m-%d %H:%M:%S.%f"))

date_str = "2023-07-15 18:25:10.121473"
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

# Получаем день недели (0 - понедельник, 6 - воскресенье)
weekday_num = date_obj.weekday()

# Список названий дней недели
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

# Выводим результат
print(f"Дата {date_str} — это {weekdays[weekday_num]}")

past_date = datetime.strptime("2023-06-12 15:23:45.312167", "%Y-%m-%d %H:%M:%S.%f")

# Текущая дата
current_date = datetime.now()

# Разница в днях
delta = current_date - past_date
print(f"Прошло дней: {delta.days}")
