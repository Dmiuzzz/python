from sys import argv
def salary_calc(z, a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    print(a * b + c)
salary_calc(*argv)