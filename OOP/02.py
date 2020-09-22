class x:
    HREN = 299 # Если атрибут капсом то нельзя его изменять(Соглашенние)

    def __init__(self, y, f):

        self.__y = y # Так можно защитить атрибут от изменений
        self._f = f # На уровне соглашенния, изменять только в наследнике


l = x(12, 3)

print(l._f)

try:
    print(l.__y) # Мы не можем влиять на этот атрибут
except AttributeError as ex:
    print("Attribute (__y) is protected")

print(l._x__y) # Так можно обойти защиту (_(Класс)__(Атрибут))
