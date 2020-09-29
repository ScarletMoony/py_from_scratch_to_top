import copy as copying

x = [1, 2, 3, [1, 2, 3]]

x_copy = x.copy()
print(x, x_copy)

x_copy[3].append(4)
print(x, x_copy)

x_copy.append(4)
print(x, x_copy)

x.append(5)
print(x, x_copy)

s_copy = copying.copy(x)
s_copy[3].append(8)
print(x, s_copy)

d_copy = copying.deepcopy(x)
d_copy[3].append(9)
print(x, d_copy)

# Модуль copy работает со всем, и с функциями, и с классами, и со всем другим
