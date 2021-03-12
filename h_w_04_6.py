a = int(input('Введите число старт '))
b = int(input('Введите число финиш '))
from itertools import count, cycle

l = []

for el in count(a):
    if el > b:
        break
    else:
        l.append(el)
        print(el)
print(l)
d = int(input("Введите количество итераций "))
c = 0
for el in cycle(l):
    if c > d:
        break
    print(el)
    c += 1
