while True:
    x = int(input())
    if x == 0:
        break

    lista = []
    for c in range(1, x + 1):
        lista.append(c)

    print(' '.join(map(str, lista)))
