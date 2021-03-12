a = 1
b = 1
goods = []
while a != 0:
    my_dict = {"название": input("Название товара "), "цена": input("Цена "),
           "количество": input("Количество "), "ед": input("единица измерения ")}
    kor = (b, my_dict)
    goods.append(kor)
    a = int(input("Введите 1 если хотите добавить ещё товар и 0 если нет "))
    b += 1
print(goods[0,1].items)
