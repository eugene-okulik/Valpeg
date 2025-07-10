temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
    34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
    29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

# Фильтруем температуры выше 28
hot_days = list(filter(lambda x: x > 28, temperatures))

print("Жаркие дни:", hot_days)

# Вычисляем самую высокую, самую низкую и среднюю температуру
max_temp = max(hot_days)
min_temp = min(hot_days)
avg_temp = sum(hot_days) / len(hot_days)

print(f"Самая высокая температура: {max_temp}")
print(f"Самая низкая температура: {min_temp}")
print(f"Средняя температура: {avg_temp:.2f}")  # Округляем до 2 знаков после запятой
