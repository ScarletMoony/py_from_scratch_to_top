x = {'A':12, 'B':2, 'C':145, 'D':222} # Обычный словарь

print(x)

print(x.get('C')) # Получить значение ключа в()

x['C'] = 135 # Изменить значение ключа

print(x)

del x['C'] # Удалить ключ

print(x)

y = x.keys() # Вывод всех лючей

print(x)
print(y)

f = list(x.keys()) # Вывод ключей как список

print(f)

print(sorted(x.keys())) # Отсортировать ключи

print('A' in x) # Проверка есть ли ключ в словаре
print('A' not in x) # Проверка нет ли ключа в словаре

z = x.values() # Выводит значения

print(z)

x.setdefault('G') # Добавляет ключ со значением (None)

print(x)

x.popitem() # Удаляет случайный элемент
x.pop('B') # Удаляет элемент в скобках

print(x)

for k, v in x.items(): # Так можно перебрать словарь
    print(f'{k}: {v}')
