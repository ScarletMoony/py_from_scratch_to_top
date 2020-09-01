set1 = set()
set1 = {1, 2, 3, 4, 5} # Множество, имеет неповторяющиеся элементы

print(set1)

set1.add(6) # Добавление элемента, если он еще не существует

print(set1)

set1.add(1)

print(set1)

set2 = {1, 2, 3, 4, 5, 6, 7, 8}

print(set1.issubset(set2)) # Проверяет есть ли все значения set1 в set2
print(set2.issuperset(set1)) # Проверяет есть ли все значения set2 в set1 и +
# другие элементы которых нет в set1(ОБЯЗАТЕЛЬНО, иначе set2 не будет superset)

print(set1.isdisjoint(set2)) # Проверяет полностью ли отличаються множества

set3 = set1.union(set2) # Обьединяет множества в одно

print(set1)
print(set2)
print(set3)
