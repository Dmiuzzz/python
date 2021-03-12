def int_func(t): #ф делает заглавной первую букву в строке из 1 слова
    t_l = list(t) #перевод строки в список для работы с первой буквой
    tr = int(ord(t_l[0])) - 32
    t_l[0] = chr(tr)
    t = "".join(t_l) #перевод измененого списка в строку
    return t
def all_int_func(t_t):
    t_n = []
    t_l = t_t.split() #перевод строки в лист по разделителю
    for x in t_l:
        t_n.append(int_func(x)) #прогоняем каждое слово ч/з int_func() и добавляем в список t_n
    t_t = " ".join(t_n)
    return t_t
print(all_int_func('text shmext кекс'))

