from functools import reduce


def mult(a,b):
    return a * b
a = [el for el in range(100, 1001) if el % 2 == 0]
res = reduce(mult, a)
print(res)