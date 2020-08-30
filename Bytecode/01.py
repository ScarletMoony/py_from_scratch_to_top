import sys

print(sys.getdefaultencoding()) # Показывает какая стандартная кодировка

print(ord ('a')) # Показывает как символ выглядит в кодировке
print(chr(97)) # Показывает какой символ закодирован по тем что в ()

y = 'Hello'

x = y.encode('utf8') # Кодирует содержимое строки
print(x.decode('utf8')) # Разкодирует содержимое строки

print(y)
print(type(x))
print(x)

for b in x: # Здесь я перебираю все элементы закодированного масива из строки
    print(b) # (y) в переменную (х) и вывожу их

print(bytearray(x)) # С помощью этого можно изменять значения элементов в
# закодированном массиве

# Пример кодирования данных

d = [1, 23] # Типа закодированные данные

with open ('file/btest.bin', 'w+b') as file: # Записываем закодированые данные
    file.write(bytes(d))

with open ('file/btest.bin', 'rb') as file: # Считываем их
    data = file.read()
    for dat in data:
        print(int(dat)) # И выводим
