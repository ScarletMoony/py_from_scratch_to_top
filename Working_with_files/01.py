import os

print(os.getcwd()) # Выводит путь к текущему файлу, в котором код

#File permissions:
# 1. 'r' - read only
# 2. 'w' - write only (owerwrites all data in file or creates new one)
# 3. 'a' - append only
# 4. 'r+' - read + write
# 5. 'w+' - read + write (owerwrites all data in file or creates new one)

with open('files/some.txt', 'r+') as file: # Открываем файл как file
    x = file.read() # Записывает данные из файла в переменную
    print(x)
    y = file.readlines() # Записывает данные из файла в перемменую в виде
    # списка
    print(y)
    file.seek(0) # Переводит курсор открытого файла в начало
    y = file.readlines()
    print(y)
    print(file.closed) # Проверяет закрыт ли файл
    file.close() # Закрывает файл
    print(file.closed)
