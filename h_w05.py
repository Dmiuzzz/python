my_list = [7, 5, 3, 3, 2]
print(my_list)
y = int(input('Введите число '))
a = 0 #переменная для вычисления позиции в списке
for x in my_list:
    if x < y:
        break
    a += 1
my_list.insert(a, y)
# print(a)
print(my_list)
