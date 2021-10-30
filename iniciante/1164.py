n = int(input())

for c in range(0, n):
    x = int(input())
    lista = []
    for i in range(1, x):
        if x % i == 0:
            lista.append(i)
    soma = sum(lista)

    if soma == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')