print('Введите элементы списка разделяя их кл "Ввод" в конце списка кл"Пробел" и кл"Ввод"')
my_list = []
x = 0
c = 0
while x != ' ':
    x = input()
    if x == ' ':
        break
    c += 1
    my_list.append(x)
# print(c)
a = 0
while a < c-1:
    my_list[a], my_list[a+1] = my_list[a+1], my_list[a]
    a += 2

print(my_list)