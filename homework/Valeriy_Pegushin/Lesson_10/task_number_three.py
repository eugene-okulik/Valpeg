# Определяем декоратор operation_controller, который будет управлять выбором операции
def operation_controller(func):
    # Внутренняя функция-обертка, которая принимает аргументы и определяет операцию
    def wrapper(first, second, operation=None):
        # Если операция не указана (None), определяем ее автоматически
        if operation is None:
            # Если числа равны, выбираем сложение (+)
            if first == second:
                operation = '+'
            # Если первое число больше второго, выбираем вычитание (-)
            elif first > second:
                operation = '-'
            # Если второе число больше первого, выбираем деление (/)
            elif second > first:
                operation = '/'
            # Если хотя бы одно число отрицательное, выбираем умножение (*)
            if first < 0 or second < 0:
                operation = '*'
        # Вызываем исходную функцию calc с выбранной операцией
        return func(first, second, operation)
    # Возвращаем функцию-обертку
    return wrapper

# Применяем декоратор к функции calc
@operation_controller
# Функция calc, которая выполняет арифметические операции
def calc(first, second, operation):
    # Если операция '+', возвращаем сумму чисел
    if operation == '+':
        return first + second
    # Если операция '-', возвращаем разность чисел
    elif operation == '-':
        return first - second
    # Если операция '*', возвращаем произведение чисел
    elif operation == '*':
        return first * second
    # Если операция '/', возвращаем частное чисел
    elif operation == '/':
        return first / second
    # Если операция не поддерживается, вызываем ошибку
    else:
        raise ValueError("Неподдерживаемая операция")

# Запрашиваем у пользователя ввод двух чисел
try:
    # Преобразуем ввод в тип float (дробное число)
    first_num = float(input("Введите первое число: "))
    second_num = float(input("Введите второе число: "))
# Если введено не число, обрабатываем ошибку и завершаем программу
except ValueError:
    print("Ошибка: введите числа!")
    exit()

# Вызываем функцию calc (с автоматическим выбором операции благодаря декоратору)
result = calc(first_num, second_num)
# Выводим результат
print(f"Результат: {result}")
