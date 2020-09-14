def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide to zero") # Выдаст ошибку
    return x/y                             # которую нам надо с нашим описанием

print(divide(2, 0))
