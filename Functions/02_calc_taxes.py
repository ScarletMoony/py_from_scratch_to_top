def calc_taxes(*args): # (*args) позволяет передавать сколько угодно аргументов
    for x in args:
        print(x)
    print(sum(args))
    return (f'Your full payment = {sum(args)}, your tax is: {round(sum(args)*0.06, 1)}')

print(calc_taxes(10, 29, 235))
