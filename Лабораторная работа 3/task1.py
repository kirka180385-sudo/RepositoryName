class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self.name

    @property
    def author(self):
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return None

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError(" Должно быть типа int")
        if value <= 0:
            raise ValueError("Должно быть положительным числом ")
        self.pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц{self.pages}"

    def __repr__(self):
        """Переопределяем для включения pages"""
        return f"PaperBook(name='{self.name}', author='{self.author}', pages={self.pages})"
    

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
        
    @property
    def duration(self):
        return None

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError("Должно быть типа float")
        if value <= 0:
            raise ValueError("Должно быть положительным числом")
        self.duration = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность{self.duration}"

    def __repr__(self):
        """Переопределяем для включения duration"""
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.duration})"
