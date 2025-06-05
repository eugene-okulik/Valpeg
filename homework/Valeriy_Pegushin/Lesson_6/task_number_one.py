text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
        " Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

# Преобразуем строку в список
words = text.split()

# Создаём пустой список для хранения изменённых слов
result = []

# Для каждого слова проверяем, заканчивается ли оно на запятую или точку
for word in words:
    if word[-1] in {',', '.'}:

        # Если да, то 'ing' добавляется перед знаком препинания
        modified_word = word[:-1] + 'ing' + word[-1]

    # Иначе 'ing' просто добавляется в конец слова
    else:
        modified_word = word + 'ing'

    # Добавляем измененные слова в список
    result.append(modified_word)

# Все слова преобразуем обратно в строку и выводим получившийся текст
print(' '.join(result))
