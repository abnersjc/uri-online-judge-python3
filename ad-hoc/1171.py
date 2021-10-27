n = int(input())
lista = []
for d in range(0, n):
    x = int(input())
    lista.append(x)

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista_ordenada = remove_repetidos(lista)

for i in range(0, len(lista_ordenada)):
    print('{} aparece {} vez(es)'.format(lista_ordenada[i], lista.count(lista_ordenada[i])))