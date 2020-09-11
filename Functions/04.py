def x(y):
    return (y*y)

f = [1, 3, 4, 63]

l = list(map(x, f)) # (map) проходится функцией (x) по списку (f) циклом (for)

print(l)
