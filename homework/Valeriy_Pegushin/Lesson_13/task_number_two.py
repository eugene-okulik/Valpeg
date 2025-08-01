# Импорт модуля для работы с операционной системой
import os
# Импорт классов datetime и timedelta из модуля datetime
from datetime import datetime, timedelta

# Получение пути к директории текущего файла
base_path = os.path.dirname(__file__)
# Получение пути к родительской директории (на два уровня выше)
homework_path = os.path.dirname(os.path.dirname(base_path))
# Формирование полного пути к файлу data.txt
eugene_okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

# Список названий дней недели на русском
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

with open(eugene_okulik_file_path) as file:
    # Чтение файла
    # print(file.read())
    # Чтение файла построчно
    for line in file:
        # Удаление лишних пробелов и переносов строк
        line = line.strip()
        # Разделение строки на части по пробелам
        parts = line.split()
        # Проверка, что в строке достаточно частей (минимум 3)
        if len(parts) >= 3:
            # Соединение второй и третьей части строки (дата и время)
            date_str = parts[1] + " " + parts[2]
            try:
                # Преобразование строки с датой в объект datetime
                date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

                # 1. Для даты 2023-11-27 - добавляем 7 дней
                if date_str.startswith("2023-11-27"):
                    # Добавление 7 дней к дате
                    new_date = date_obj + timedelta(days=7)
                    # Вывод новой даты
                    print(f"Дата на неделю позже (через 7 дней): {new_date}")

                # 2. Для даты 2023-07-15 - определяем день недели с русскими названиями
                elif date_str.startswith("2023-07-15"):
                    # Получение номера дня недели (0-6)
                    weekday_num = date_obj.weekday()
                    # Вывод названия дня недели на русском
                    print(f"Дата {date_str} — это {weekdays[weekday_num]}")

                # 3. Для даты 2023-06-12 - вычисляем сколько дней прошло
                elif date_str.startswith("2023-06-12"):
                    # Вычисление разницы между текущей датой и указанной в днях
                    days_passed = (datetime.now() - date_obj).days
                    # Вывод количества прошедших дней
                    print(f"Дней прошло с {date_str}: {days_passed}")


            # Обработка ошибки при парсинге даты
            except ValueError as e:
                # Вывод сообщения об ошибке
                print(f"Ошибка при разборе даты: {e}")
