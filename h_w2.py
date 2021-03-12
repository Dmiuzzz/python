print("Введите время в секудах ")
time =int(input())
h = time//3600
m = time%3600//60
s = time%60
print(f'{h:02}:{m:02}:{s:02}')