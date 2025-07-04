# Импортируем встроенный модуль random из стандартной библиотеки Python
import random

# Запрашиваем зарплату у пользователя
salary = int(input("Введите вашу зарплату: "))

# Случайно определяем, будет ли бонус
bonus = random.choice([True, False])

if bonus:  # Если бонус равен True (если бонус назначен)
    bonus_percent = random.randint(1, 50)  # Выбираем случайный процент бонуса от 1% до 50%
    bonus_amount = salary * bonus_percent // 100  # Вычисляем сумму бонуса (целое число)
    total = salary + bonus_amount  # Добавляем бонус к зарплате
else:
    total = salary

# Форматируем вывод с символом доллара
print(f"${total}")
