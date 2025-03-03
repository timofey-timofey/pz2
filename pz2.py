class PostalAddress:
    def __init__(self, street, house, apartment):
        self._street = street
        self._house = house
        self._apartment = apartment

    def street(self):
        return self._street

    def street(self, value):
        self._street = value

    def house(self):
        return self._house

    def house(self, value):
        self._house = value

    def apartment(self):
        return self._apartment

    def apartment(self, value):
        self._apartment = value

# Создаем экземпляры класса
address1 = PostalAddress("Ленина", 12, 34)
address2 = PostalAddress("Пушкина", 5, 10)

# Выводим значения свойств объектов
print(f"Адрес 1: Улица - {address1.street}, Дом - {address1.house}, Квартира - {address1.apartment}")
print(f"Адрес 2: Улица - {address2.street}, Дом - {address2.house}, Квартира - {address2.apartment}")

# Изменяем значения полей
address1.street = "Карла Маркса"
address2.apartment = 15

# Выводим обновленные адреса
print(f"Обновленный Адрес 1: Улица - {address1.street}, Дом - {address1.house}, Квартира - {address1.apartment}")
print(f"Обновленный Адрес 2: Улица - {address2.street}, Дом - {address2.house}, Квартира - {address2.apartment}")

