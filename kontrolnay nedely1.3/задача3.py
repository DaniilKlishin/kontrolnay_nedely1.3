import math

p = int(input("Показатель степени: "))
n = int(input("Предел: "))
 
i = 1
while i ** p <= n:
    print(i ** p, end=' ')
    i += 1
 
print("Последнее число, возведенное в степень:", i - 1)