set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
set3 = set1.intersection(set2) # Показывает элементы set1 которые есть в set2

print(set3)

set4 = set1.difference(set2) # Показывает элементы set1 которых нет в set2

set5 = set1.symmetric_difference(set2) # Показывает все отличия между
# множествами

print(set4)
print(set5)

set1.update(set2) # Перезаписывает значения set2 в set1

print(set1)

set1.remove(4) # Удаляет элемент, ошибка при удалении несуществующего

print(set1)

set1.discard(3) # Удаляет элемент без ошибок

print(set1)

x = set1.pop() # Удаляет случайный элемент и записывает его в x

print(set1)
print(x)

set1.clear() # Очищает множество

print(set1)

x = range(1, 100) # Создает массив от 1 до 99

for i in x:
    print(i)
