# TODO Написать 3 класса с документацией и аннотацией типов
class Microphone:
    """
    Документация на класс.
    Класс описывает модель микрофона.
    """
    def __init__(self, brand: str, type_micro: str, price: int, number_song: int) -> None:
        """
        Инициализация экземпляра класса.
        :param brand: Брэнд микрофона(название)
        :param type_micro: Направленность микрофона
        :param price: Цена микрофона
        :param number_song: Количество записанных песен на этот микрофон

        Например:
        >>> micro = Microphone("Neumann U 87 Ai", "Конденсаторный", 20000, 0)
        """
        if not isinstance(brand, str):
            raise TypeError("Значение должно быть типа str")
        self.brand = brand
        if not isinstance(type_micro, str):
            raise TypeError("Значение должно быть типа str")
        self.type_micro = type_micro
        if not isinstance(price, int):
            raise TypeError("Значение должно быть типа int")
        self.price = price
        if not isinstance(number_song, int):
            raise TypeError("Значение должно быть типа int")
        self.number_song = number_song

    def use_micro(self, add_song: int) -> int:
        """
        Функция, которая считает количество песен, записанных на этот микрофон
        :param add_song: Увеличивает число записанных песен на этот микрофон
        :raise ValueError: Количество добавляемых песен отрицательна
        :return: Новое количество записанных песен
        Например:
        >>> total = Microphone("Neumann U 87 Ai", "Конденсаторный", 400000, 0)
        >>> total.use_micro(4)
        4
        >>> total.use_micro(1)
        5
        """
        if not isinstance(add_song, int):
            raise TypeError("Должно быть значение типа int")
        if add_song < 0:
            raise ValueError("Значение должно быть неотрицательным")
        self.number_song += add_song #Новое количество песен
        ...
    def current_status(self) -> int:
        """
        Функция, которая определяет текущее состояние записанных песен
        :return: Количество записанных песен
        Пример:
        >>> songs = Microphone("Neumann U 87 Ai", "Конденсаторный", 400000, 5)
        >>> songs.current_status()
        5
        """
    ...


class BankAccount:
    def __init__(self, account_holder: str, balance: float, currency: str = "RUB") -> None:
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_holder: Владелец счета
        :param balance: Баланс счета
        :param currency: Валюта счета (по умолчанию RUB)

        Примеры:
        >>> account = BankAccount("Андрей Классов", 15000.50)  # инициализация экземпляра класса
        >>> account_usd = BankAccount("John Doe", 1000.0, "USD")
        """
        if not isinstance(account_holder, str):
            raise TypeError("Имя владельца должно быть типа str")
        if len(account_holder.strip()) == 0: #Для удаления пробелов, вдруг пользователь введет пробелы
            raise ValueError("Имя владельца не может быть пустым")
        self.account_holder = account_holder

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числового типа")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = float(balance)

        if not isinstance(currency, str):
            raise TypeError("Валюта должна быть типа str")
        if len(currency.strip()) == 0:
            raise ValueError("Валюта не может быть пустой")
        self.currency = currency

    def deposit(self, amount: float) -> float:
        """
        Функция, которая добавляет средства на счет

        :param amount: Сумма для пополнения
        :raise ValueError: Если сумма пополнения отрицательная
        :return: Новый баланс счета

        Примеры:
        >>> account = BankAccount("Иван Иванов", 15000.50)
        >>> account.deposit(5000.0)
        20000.5
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числового типа")
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")

        self.balance += amount


    def withdraw(self, amount: float) -> float:
        """
        Функция, которая снимает средства со счета

        :param amount: Сумма для снятия
        :raise ValueError: Если сумма снятия превышает баланс или отрицательная
        :return: Новый баланс счета

        Примеры:
        >>> account = BankAccount("Иван Иванов", 15000.50)
        >>> account.withdraw(3000.0)
        12000.5
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числового типа")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")

        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount') -> None:
        """
        Функция для перевода средств на другой счет

        :param amount: Сумма перевода
        :param target_account: Целевой счет для перевода
        :raise ValueError: Если валюты счетов не совпадают или недостаточно средств

        Примеры:
        >>> account1 = BankAccount("Иван Иванов", 15000.50)
        >>> account2 = BankAccount("Петр Петров", 5000.0)
        >>> account1.transfer(3000.0, account2)
        """
        if self.currency != target_account.currency:
            raise ValueError("Нельзя переводить средства между счетами в разных валютах")

        self.withdraw(amount)
        target_account.deposit(amount)


class WaterBottle:
    def __init__(self, volume: float, current_water: float = 0) -> None:
        """
        Создание и подготовка к работе объекта "Бутылка с водой"

        :param volume: Объем бутылки в литрах
        :param current_water: Текущее количество воды в литрах (по умолчанию 0)

        Примеры:
        >>> bottle = WaterBottle(1.5)  # пустая бутылка объемом 1.5 литра
        >>> bottle_full = WaterBottle(1.5, 1.5)  # полная бутылка 1.5 литра
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем должен быть числом")
        if volume <= 0:
            raise ValueError("Объем должен быть положительным")
        self.volume = float(volume)

        if not isinstance(current_water, (int, float)):
            raise TypeError("Количество воды должно быть числом")
        if current_water < 0:
            raise ValueError("Количество воды не может быть отрицательным")
        if current_water > volume:
            raise ValueError("Количество воды не может превышать объем бутылки")
        self.current_water = float(current_water)

    def add_water(self, amount: float) -> float:
        """
        Функция, которая добавляет воду в бутылку

        :param amount: Количество воды для добавления в литрах
        :raise ValueError: Если после добавления воды превышается объем бутылки
        :return: Текущее количество воды в бутылке после добавления

        Примеры:
        >>> bottle = WaterBottle(1.0)
        >>> bottle.add_water(0.3)
        0.3
        >>> bottle.add_water(0.5) #  к 0.3л добавили еще 0.5л
        0.8
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество воды должно быть числом")
        if amount < 0:
            raise ValueError("Количество воды должно быть неотрицательным")

        new_amount = self.current_water + amount
        if new_amount > self.volume:
            raise ValueError(f"Нельзя добавить больше {self.volume - self.current_water:.2f} литров")

        self.current_water = new_amount


    def drink_water(self, amount: float) -> float:
        """
        Функция, которая позволяет выпить воду из бутылки

        :param amount: Количество воды для выпивания в литрах
        :raise ValueError: Если пытаемся выпить больше воды, чем есть в бутылке
        :return: Оставшееся количество воды в бутылке

        Примеры:
        >>> bottle = WaterBottle(1.0, 0.8)
        >>> bottle.drink_water(0.3)
        0.5
        >>> bottle.drink_water(0.2)
        0.3
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество воды должно быть числом")
        if amount < 0:
            raise ValueError("Количество воды должно быть неотрицательным")

        if amount > self.current_water:
            raise ValueError(f"Нельзя выпить больше {self.current_water:.2f} литров")

        self.current_water -= amount

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
