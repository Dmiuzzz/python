# Через list
# season = ['зима', 'весна', 'лето', 'осень']
# print('Введите месяц цифрами от 1 до 12')
# m = int(input())
# if m < 3 or m == 12:
#     print(season[0])
# elif m < 6 and m > 2:
#     print(season[1])
# elif m < 9 and m > 5:
#     print(season[2])
# elif m < 12 and m > 8:
#     print(season[3])
# else: print ('ERROR')

# Через dict
dict_season = {
    1: "зима",
    2: "зима",
    12: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень"
}
season = int(input("Введите месяц цифрами от 1 до 12: "))
print(dict_season[season])
