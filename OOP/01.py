class Character: # Создаем класс

    def __init__(self, race): #Конструктор класса(Класс может иметь только один)
        self.race = race # Присваивание переменной обьекту

hero = Character("Orc") # Создание обьекта

print(hero.race) # Вывод элемента обьекта
