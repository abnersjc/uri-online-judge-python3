t = int(input())
lista = []
for n in range(0, 1000):
    for i in range(0, t):
        lista.append(i)

    print('N[{}] = {}'.format(n, lista[n]))