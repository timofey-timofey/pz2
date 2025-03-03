class PostalAddress:
    def __init__(self, street, house, apartment=None):
        self.street = street
        self.house = house
        self.apartment = apartment

    def street(self):
        return self._street

    def street(self, value):
        if not value or not value.strip():
            raise ValueError("Улица не может быть пустой.")
        if not (value.startswith("ул") or value.startswith("пр") or value.startswith("пер")):
            raise ValueError("Тип улицы должен начинаться с 'ул', 'пр' или 'пер'.")
        self._street = value

    def house(self):
        return self._house

    def house(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Номер дома должен быть положительным целым числом.")

        street_type = self.street[:2]

        if street_type == "пер" and not (1 <= value <= 30):
            raise ValueError("На переулке номер дома должен быть от 1 до 30.")
        elif street_type == "ул" and not (1 <= value <= 100):
            raise ValueError("На улице номер дома должен быть от 1 до 100.")
        elif street_type == "пр" and not (1 <= value <= 1000):
            raise ValueError("На проспекте номер дома должен быть от 1 до 1000.")

        self._house = value

    def apartment(self):
        return self._apartment

    def apartment(self, value):
        if self.house is not None and value is not None:
            raise ValueError("Для частного дома не указывается квартира.")
        self._apartment = value


# Программа для демонстрации работы класса
try:
    address1 = PostalAddress("ул Ленина", 12, 34)
    address2 = PostalAddress("пр Красный", 100, None)

    print(f"Адрес 1: Улица - {address1.street}, Дом - {address1.house}, Квартира - {address1.apartment}")
    print(f"Адрес 2: Улица - {address2.street}, Дом - {address2.house}, Квартира - {address2.apartment}")

    # Проверка на случай, если мы попытаемся установить неправильные значения
    address1.street = "пер Невский"  # допустимо
    address1.house = 5  # допустимо
    address1.apartment = 101  # вызовет ошибку

except ValueError as ve:
    print(f"Ошибка: {ve}")
