# open("file pass", opening mode like "r", buffering, encoding, errors)

# Режимы отркывания:
#   "r" = открыть только для чтения
#   "w" = открыть для записи, если файл не существует то он его создаст, все что было в файле удалится
#   "x" = создание эксклюзивного файла, если файл существует то выдасться ошибка
#   "a" = добавляет запись в конец файла "appends"
#   "b" = запускает в бинарном режиме
#   "t" = текстовый режим, только чтение
#   "w+" и "r+" = работают также но не удаляют все содержиммое, и в том и в том можно производить и чтение и запись
#   "r+b" и "w+b" = работают также но в бинарном режиме

# Режимы буферизации:
#   0 = выключает буферизацию, только в бинарном режимеonly when writing.
#   1 = линейная буферизация, только в текстовом режиме
#   -1 = стандартная буферизация
#   >1 = фиксированный размер блока буферизации

# Encoding имя кодировки, по дефолту используеться кодировка вашего ПК

# error attributes:
#   'strict' = raises a ValueError if wrong encoding
#   'ignore' = ignore errors
#   'replace' = replaces damaged data with '?'
#   'surrogateescape' = represents incorrect bytes as code points, then turning them to correct. Useful for unknown
#      encode
#   'xmlcharrefreplace' = only when writing. Chars what not supported in enconding will be replaced with XML chars
#   'backslashreplace' = replaced damaged data with python backslashed escape sequences
#   'namereplace' = only when writing. Replaces unsupported chars with \n escape sequences

handle = open("AdditionalFiles/test.txt", "r")

data = handle.read()

print(data)

handle.close()

handle = open("AdditionalFiles/test.txt", "r")

data = handle.readline()

print(data)

data = handle.readlines()

print(data)
handle.close()


