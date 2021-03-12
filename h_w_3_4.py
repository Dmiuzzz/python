def my_func(x, y):
#Через цикл
#     s = 1 / x
#     while y < -1:
#         s = s / x
#         y += 1
#Через оператор
    s = x ** y

    return s
print(my_func(10, -4))