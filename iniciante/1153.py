from math import prod

n = int(input())

lista = []

for i in range(1, n):
    f = n - i
    lista.append(f)

print(n * (prod(lista)) * 1)