# Импорт модуля для работы с операционной системой (файлы, пути и т. д.)
import os
# Импорт классов datetime и timedelta из модуля datetime для работы с датами и временем
from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)
# file_path = f'{base_path}/data.txt'
# file_path = os.path.join(base_path, 'data.txt')
# new_file_path = os.path.join(base_path, 'data2.txt')
# print(file_path)


homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
# print(eugene_okulik_file_path)


with open(eugene_okulik_file_path) as eugene_okulik_file:
    print(eugene_okulik_file.read())
