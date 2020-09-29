x = [1, 2, 3]

print(x)

print(repr(x))

print(eval(repr(x)) == x)

from datetime import datetime

dt = datetime.now()

print(dt)

print(repr(dt))

class c:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"c({self.x}, {self.y})"

    def __str__(self):
        return f'printed sum = {self.x + self.y}'

    def __eq__(self, other):
        if isinstance(other, c):
            return self.x == other.x and self.y == other.y


c1 = c(2, 5)

print(c1)

print(repr(c1))

f1 = eval(repr(c1))

print(f1)

print(type(c1))
print(type(f1))

print(c1 == f1)
