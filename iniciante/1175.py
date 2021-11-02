lista = []
for i in range(0, 20):
    n = int(input())
    lista.insert(0, n)
    
for d in range(0, 20):
    print('N[{}] = {}'.format(d, lista[d]))