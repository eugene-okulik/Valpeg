# Базовый класс для всех цветов
class Flower:
    # Конструктор класса Flower
    def __init__(self, name, color, lifespan_days, stem_length, price):
        self.name = name          # Название цветка
        self.color = color       # Цвет цветка
        self.lifespan = lifespan_days  # Срок жизни в днях
        self.stem_length = stem_length  # Длина стебля в см
        self.price = price       # Цена цветка

    # Строковое представление цветка
    def __str__(self):
        return f"{self.name} ({self.color}), {self.price} руб."


# Класс розы (наследуется от Flower)
class Rose(Flower):
    def __init__(self, color, stem_length=50.0, has_thorns=True):
        super().__init__("Роза", color, 7, stem_length, 100)
        self.has_thorns = has_thorns  # Наличие шипов у розы


# Класс тюльпана (наследуется от Flower)
class Tulip(Flower):
    def __init__(self, color, stem_length=30.0):
        super().__init__("Тюльпан", color, 5, stem_length, 40)


# Класс для работы с букетами цветов
class Bouquet:
    def __init__(self):
        self.flowers = []  # Список цветов в букете

    # Добавление цветка в букет
    def add_flower(self, flower_to_add):
        self.flowers.append(flower_to_add)

    # Расчет общей стоимости букета
    def total_price(self):
        return sum(f.price for f in self.flowers)  # Используем краткое имя f

    # Расчет среднего срока жизни букета
    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(f.lifespan for f in self.flowers) / len(self.flowers)

    # Сортировка цветов по цене
    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price)

    # Сортировка цветов по сроку жизни
    def sort_by_lifespan(self):
        self.flowers.sort(key=lambda x: x.lifespan)

    # Сортировка цветов по длине стебля
    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length)

    # Поиск цветов по цвету
    def find_by_color(self, target_color):
        return [fl for fl in self.flowers
                if fl.color.lower() == target_color.lower()]

    # Поиск цветов в ценовом диапазоне
    def find_in_price_range(self, price_min, price_max):
        return [fl for fl in self.flowers
                if price_min <= fl.price <= price_max]

    # Строковое представление букета
    def __str__(self):
        return (f"Букет ({len(self.flowers)} цветов)\n"
                f"Общая стоимость: {self.total_price()} руб.\n"
                f"Средний срок жизни: {self.average_lifespan():.1f} дней")


# Основной блок выполнения
if __name__ == "__main__":
    # Создаем коллекцию цветов
    flower_collection = [
        Rose("красный", 60),
        Rose("белый", 45, False),
        Tulip("жёлтый", 35),
        Tulip("красный", 25)
    ]

    # Формируем букет
    my_bouquet = Bouquet()
    for flower in flower_collection:
        my_bouquet.add_flower(flower)

    # Выводим информацию о букете
    print(my_bouquet)

    # Сортируем и выводим по цене
    my_bouquet.sort_by_price()
    print("\nПосле сортировки по цене:")
    for item in my_bouquet.flowers:
        print(item)

    # Ищем и выводим красные цветы
    print("\nКрасные цветы в букете:")
    for red_flower in my_bouquet.find_by_color("красный"):
        print(red_flower)
