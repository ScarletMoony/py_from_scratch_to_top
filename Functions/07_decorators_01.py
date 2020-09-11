def func_log(func):      #Пишем функцию, которая потом станет декоратором
    def wrap():
        print(f'Started {func}')
        func()
        print(f'{func} finished it\'s work')
    return wrap

@func_log # Так мы применяем функцию как декоратор
def hello():
    print('Hello!')

hello()

print(help(hello)) # Здесь мы видим что функция(hello) это на самом деле
# функция(wrap). Как это пофиксить в следующем уроке
