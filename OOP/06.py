import webbrowser # Модуль для открытия ссылок

class Road():

    def __init__(self, length):
        self.length = length

    def __len__(self): # Дандер методы, влияют на функциональность класса
        return self.length

    def __str__(self):
        return f'A road of length: {self.length}'

    def __del__(self):
        print(f'The road has been destroyed')

r = Road(100)

print(len(r))

print(r)

del r

print("Do you want to see documentation about dunder methods?")

x = input()

if x == 'Y' or x == 'y': # Переход по ссылке для документации про дандер методы
    webbrowser.open('https://docs.python.org/3/reference/datamodel.html', new=2)
else:
    exit()
