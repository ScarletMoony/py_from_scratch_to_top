def f (age):
    return (age >= 18)

ages = [14, 18, 23, 45]

print(list(filter(f, ages))) # (filter) сортирует список (ages) функцией (f)

x = lambda age1: age1 >= 18 # Лямбда, это функция в одну строку

print(list(filter(x, ages)))
