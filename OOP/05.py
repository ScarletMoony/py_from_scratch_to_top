from abc import ABC, abstractmethod # Импорт библиотек для абстрактных класов

class Shape(ABC): # Создание абстрактного класса

    def __init__(self):
        super().__init__() # Обязательный вызов для абстрактного класса

    @abstractmethod # Абстрактный метод, его нужно обязательно переопределять
    def perimeter(self):
        pass

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self): # ОБЯЗАТЕЛЬНО переопределять иначе будет ошибка
        print (f'Perimeter is {self.a + self.b + self.c}')

t = Triangle(12, 3, 4)

t.perimeter()
