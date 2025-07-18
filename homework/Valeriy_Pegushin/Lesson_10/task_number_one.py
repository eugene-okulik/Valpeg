# finish_me — это функция-декоратор, которая принимает другую функцию (func) в качестве аргумента

def finish_me(func):

    # Внутри декоратора определяется функция-обёртка (wrapper), которая:
    # Вызывает оригинальную функцию (func) с переданными аргументами (*arguments, **options)

    def wrapper(*arguments, **options):
        result = func(*arguments, **options)  # Передаём аргументы как есть
        print("finished")  # Печатает "finished" после выполнения функции
        return result  # Возвращаем результат исходной функции `func`, чтобы он не потерялся после декорирования
    return wrapper  # Декоратор возвращает функцию-обёртку (wrapper)


@finish_me  # Декоратор @finish_me применяется к функции example
def example(text):  # При вызове example(text) выполняется не сама функция example, а её обёрнутая версия (wrapper)
    print(text)


example('print me')
