x = "Hello"

x.lower()  # возвращает новую строку с нижним регистром

print(x)

print(x.capitalize())  # возвращает все символы с маленькой и первый символ с большой

print(x.count('l'))  # возвращает количестао символов в строке

print(x.center(100, "|"))  # возвращает строку по центру, первое это сколькими символами запролнять для ценртализации

# второе это какими символами

print(x.encode())  # возвращает строку в битовом представлении

x = 'Hello'

print(x.endswith('o'))  # Проверяет заканчиваеться ли строка символом

print(x.casefold())  # возвращает новую строку с нижним регистром

some = "Hello, my name is Alex"

print(some.find('is', 1, 20))  # возвращает индекс символа, 1 это с какого символа начинать, 2 с какого заканчивать

tabs = "H\te\tl\tl\to\t"  # \t ставит таб

print(tabs, tabs.expandtabs(30))  # возвращает строку с расширенными табами

print(x.index('l', 1, 20))  # возвращает индекс символа с 1 по 20

print(x.isalnum())  # проверяет все ли символы только буквы и цифры без спец символов

print(x.isalpha())  # проверяет все ли символы буквы

print(x.isdecimal())  # всче ли символы в десятичном виде

print(x.isdigit())  # вся ли строка из цифр

print(x.isidentifier())  # Проверяет являеться ли строка правильным идентификаротом, не может начмнаться с цифры,

# не может содержать спец символы кроме '_'

print(x.islower())  # вся ли строка в нижнем регистре

print(x.isnumeric())  # вся ли строка из цифр

print(x.isprintable())  # всю ли строку можно вывести с помощью print

print(x.isspace())  # вся ли строка состоит из пробелов

print(x.istitle())  # все ли слова начинаються с большой буквы, а остальное с маленькой

print(x.isupper())  # вся ли строка в врехнем регистре

it1 = ['sel', 'if']

print(x.join(it1))  # добавляет элемемты со списка в строку, строка являеться разделителем

print(x.lower())  # возвращает все символы в нижнем регистре

print(x.lstrip())  # Разделяет строку по символу, по дефолту удаляет пробеллы

mytable = x.maketrans("H", "P")  # Меняет символ первый на второй, для расшифровки x.translate

print(x.translate(mytable))  # Расшифровует x.maketrans

print(some.partition('name'))  # Разделяет строку на 3 части, до и после того что в скобках

print(x.replace('l', 's', 1))  # Заменяет первый символ на второй, 3 агрумент это сколько первых символов менять

print(x.rfind('l', 1, 5))  # Передает индекс символа

print(x.rindex('l', 1, 5))  # Передает индекс символа

print(x.rjust(100, '|'))  # первое это сколько символов ставить, второе это какой символ, по дефолту пробел

tup1 = (1, 2, 3)

print(x.rpartition(some))  # Разделяет строку на 3 части, до и после того что в скобках

print(some.split(', ', 1))  # Разделяет строку по переданному символу и прередает список

print(x.splitlines(True))  # Разделяет строку по переходу на новую строку и передает список

print(x.startswith('H', 0, 2))  # Проверяет начинается ли строка с символа

x2 = '           f          '

x3 = x2.strip()   # Удаляет пробелы со строки

print(x3)

print(x.swapcase())  # Пеняет регистр всех символов на обратный

print(x.title())  # Меняет первую букву каждого слова в строке на верний регистр

print(x.upper())  # Меняет строку полностью на верхний регистр

print(x.zfill(20))  # Заполняет строку нулями с начала, мы передаем количество нулей
