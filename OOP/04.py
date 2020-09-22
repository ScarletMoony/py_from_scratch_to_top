class x: # Клас от которого наследуемся

    def __init__(self):
        print("X created")

    def count(self):
        print("Counted")

class y(x): # Класс наследник

    def __init__(self, a, b):
        print("Im naslednik")
        self.a = a
        self.b = b

        x.__init__(self) # Наследник может использовать функции основного класа

    def count(self): # Можно переопределять функции
        print(f'Counted a + b = {self.a + self.b}')

i = x()
p = y(5, 5) # Обязательно передать аргументы иначе будет ошибка

i.count()
p.count()
