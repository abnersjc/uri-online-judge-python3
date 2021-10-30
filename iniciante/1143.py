import math
n = int(input())
a = 1

for i in range(0, n):
    quadrado = math.pow(a, 2)
    cubo = math.pow(a, 3)
    print(f'{a} {quadrado:.0f} {cubo:.0f}')
    a += 1