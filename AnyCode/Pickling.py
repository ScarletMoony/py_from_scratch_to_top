import pickle

class Char:

    def __init__(self, health=100, gearTier=12):
        self.health = health
        self.gearTier = gearTier

c = Char()

c.health -= 10

with open ("../SomeFiles/charbit.bin", "w+b") as f:
    pickle.dump(c, f) # Создание загрузочного дамп файла

print(c.health)
c.health -= 10

with open ("../SomeFiles/charbit.bin", "rb") as f:
    pickle.load(f) # Загрузка загрузочного дамп файла

print(c.health)
