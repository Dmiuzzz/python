l = []
def fact_list(n):
    fac = 1
    for i in range(1, n+1):
        fac = i * fac
        l.append(fac)
    return l
print(fact_list(4))

# for el in fact(n)


def fact(n):
    for el in fact_list(n):
        yield el

g = fact(4)
print(g)

for el in g:
    print(el)

