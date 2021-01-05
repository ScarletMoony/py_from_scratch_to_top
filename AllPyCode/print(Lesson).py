print("Hello")

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) все что принимает print
# objects - прередает обьект который нужно вывести
# sep - передает какой разделитель будет между передаваемыми обьектами

items= [1, 2, 3]

print(items, sep=", ")
print(*items, sep=", ")

# end - передает что выводить в конце вывода

print("Hello", end="\n"+"-"*10+"\n")

# file - позволяет передать открытый файл с методом w(write) как обьект и с помощью этого записать строку в файл

f = open('AdditionalFiles/print_file.txt', 'w')

for i in range(10):
    print(f'Item {i}', file=f)

f.close()

# flush - позволяет отключить или включить буферизацию

import time

for num in range(10):
    print(num)
    time.sleep(1)

for num in range(10):
    print(num, end=' ')
    time.sleep(1)

for num in range(10):
    print(num, end=' ', flush=True)
    time.sleep(1)
