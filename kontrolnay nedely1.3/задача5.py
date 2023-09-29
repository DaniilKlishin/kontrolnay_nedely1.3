import math

N = int(input("Количество элементов: "))

a = 0
b = 1
c = 0

while c < N:
    print(a)
    g = a + b
    a = b
    b = g
    c += 1