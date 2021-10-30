while True:
    m, n = map(int, input().split())
    lista = []
    menor = 0
    maior = 0

    if m > n:
        maior = m
        menor = n
    elif n > m:
        maior = n
        menor = m
    elif n == m:
        maior = n
        menor = m

    for c in range(menor, maior +1):
        lista.append(c)
    if menor <= 0 or maior <= 0:
        break
    for elemento in lista:
        print(elemento, end=' ')
    print(f'Sum={sum(lista)}')