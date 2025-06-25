words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
# words.items() — возвращает пары (ключ, значение) из словаря
for word, count in words.items():
    # word * count — строка word повторяется count раз (например, 'I' * 3 → 'III')
    # print() — автоматически добавляет перенос строки после каждого вызова
    print(word * count)
