my_text = open("schedule.txt", "r", encoding='UTF-8')
content = my_text.readlines()           # Лист строк
# print(content)
my_text.close()
dic_sch = {}
for el in content:                    # el  ифрмация по одному предмету в строке
    num_all = 0
    el = el.split()                 # el теперь список разбитый по словам(строкам)
    for x in el:                    # x - слово(строка) из листа el
        number = ''                     # объявляю как строку, чтобы склеить число из цифр
        for i in x:                  # i - символ из строки х
            if '9' >= i >= '0':
                number += i          # собираю число из цифр
        if number != '':            # если цифр не было, пустой int(number) даст ошибку
            num_all += int(number)
    dic_sch[el[0]] = num_all
print(dic_sch)