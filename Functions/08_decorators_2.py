from functools import wraps # Здесь мы импортируем (wraps) из модуля (functools)

def func_log(func):
    @wraps(func) # Так мы делаем чтобы функция (hello) считалась сама собой
    def wrap(*args, **kwargs): # Также в (wraps) желательно использовать:
        print(f'Started {func}') #                            (*args, **kwargs)
        func(*args, **kwargs)
        print(f'{func} finished it\'s work')
    return wrap

@func_log
def hello():
    print('Hello!')

hello()

print(help(hello)) # Здесь мы видим что теперь все правильно и мы работаем с
# функцией (hello)
