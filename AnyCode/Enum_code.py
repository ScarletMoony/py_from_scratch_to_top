from enum import Enum, IntEnum, IntFlag


class c(Enum):
    X = 1
    Y = 2
    Z = 3

print(c.X)

print(c.X.name, c.X.value)

for i in c:
    print(i.name, '=', i.value)

class c2(IntEnum):
    X = 1
    Y = 2
    Z = 3

print(c2.X < c2.Y)

for i in c2:
    print(i.name, '=', i.value)

class c3(IntFlag):
    X = 1
    Y = 2
    Z = 3

f = c3.X | c3.Y

print(f, f.value)
