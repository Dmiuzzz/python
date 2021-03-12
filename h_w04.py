string = input('Введите несколько слов разделяя их пробелами ').split()
for x in string:
    print(x[:10])