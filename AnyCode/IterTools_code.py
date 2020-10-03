import itertools as itt

x = [1, 2, 3]

y = iter(x)

print(y)

for i in y:
    print(i)

en = itt.count(0, 2)

print(list(next(en) for _ in range(15)))

print(list(zip(itt.count(), ['a', 'b', 'c'])))

print(list(map(pow, range(10), itt.repeat(3))))

pno = itt.cycle([1, 2, 3])

print(list(next(pno) for _ in range(10)))

print(list(itt.accumulate([1, 2, 3, 4, 5, 6])))

x = 'ABCD'

y = ['ABCD']

print(list(itt.chain(x)))

print(list(itt.chain.from_iterable(y)))

print(list(itt.dropwhile(lambda x: x<3, [1, 2, 3, 4, 5])))

print(list(itt.takewhile(lambda x: x<3, [1, 2, 3, 4, 5])))

print(list(itt.filterfalse(lambda x: x%3==0, [1, 2, 3, 4, 5])))

print(list(itt.filterfalse(lambda x: x%3!=0, [1, 2, 3, 4, 5])))
