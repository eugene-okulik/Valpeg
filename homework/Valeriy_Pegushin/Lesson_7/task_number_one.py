# В переменной secret_number хранится загаданная цифра — 7
secret_number = 7

# Цикл while True выполняется бесконечно, пока не сработает break
while True:
    # Пользователь вводит число (input преобразуется в int)
    guess = int(input("Угадайте цифру от 0 до 9: "))
    # Если число совпадает с secret_number — выводится поздравление, и цикл завершается (break)
    if guess == secret_number:
        print("Поздравляю! Вы угадали!")
        break
    # Если не совпадает — программа пишет "Попробуйте снова!" и цикл повторяется
    else:
        print("Попробуйте снова!")
