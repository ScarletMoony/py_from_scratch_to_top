from collections import OrderedDict

d1 = {}
d1['A'] = 120
d1['B'] = 15
d1['C'] = 2

d2 = {}
d2['C'] = 2
d2['A'] = 120
d2['B'] = 15


od1 = OrderedDict()
od1['A'] = 120
od1['B'] = 15
od1['C'] = 2

od2 = OrderedDict()
od2['C'] = 2
od2['A'] = 120
od2['B'] = 15

print(d1 == d2)
print(od1 == od2)

# OrderedDict при сравнении словарей учитывает порядок элементов
