class Date:
    def __init__(self, month, day, year): # Класс может иметь только один
        self.month = month                                      # конструктор
        self.day = day
        self.year = year

    def display(self):
        return f"{self.month}-{self.day}-{self.year}"

    @classmethod # Метод похожий на конструктор
    def millenium_c(cls, month, day):
        return cls(month, day, 2000)

    @staticmethod # Метод который при наследовании будет обращаться
    def millenium_s(month, day):         # к основному классу а не к наследнику
        return Date(month, day, 2000)

d1 = Date.millenium_c(6, 9)
d2 = Date.millenium_s(6, 9)

print(d1.display())
print(d2.display())
