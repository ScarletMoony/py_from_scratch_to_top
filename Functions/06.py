x = 'hey'

def f ():
    global x # Только так можно перезаписать переменную для функции
    x = 'hi'
    print(x)

f()
