print("Введите целое положительное число")
n =int(input())
b = 0
while n >= 1:
    a = n % 10
    if b < a:
        b = a
    n = n // 10
print(b)