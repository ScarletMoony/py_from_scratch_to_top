import random

def rand_int(min, max, n):
    for i in range(n):
        yield random.randint(min, max)


for i in rand_int(1, 1000, 1000):
    print(i, end="   ")
