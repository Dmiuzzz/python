def my_fun(a, b):
    while b == 0:
        b = int(input("Введите делитель != 0 "))
    return a / b
print(my_fun(int(input("Введите делимое ")), int(input("Введите делитель != 0 "))))