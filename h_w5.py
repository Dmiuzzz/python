print("Введите выручку фирмы")
revenue =int(input())
print("Введите издержки фирмы")
costs =int(input())
result = revenue - costs
if result > 0:
    print('Фирма работает с прибылью')
    print(f'Рентабельность выручки {result/revenue}')
    print("Введите  численность сотрудников фирмы")
    num = int(input())
    print(f'Прибыль на одного сотрудника {result / num}')
else:
    print('Фирма работает с убытком')