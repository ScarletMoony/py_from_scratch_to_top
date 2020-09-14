def divide(x, y): # Обычная функция
    try:
        return x / y
    except ZeroDivisionError as ex: # Исключение ошибки
        print(f'{ex}')
    except TypeError as ex: # Можно исключать по несколько сразу
        print("Please enter a number")
    else: # Также можно использовать, работает как и в (if)
        print("Unexpected error occurred")
    finally: # Всегда выполняеться после (try/except) блока
        print("0011001100110011")

print(divide(2, 0))
