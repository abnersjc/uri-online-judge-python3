count = 0
lista = []

while count != 6:
    n_0 = float(input())
    count += 1
    if n_0 >= 0:
        lista.append(n_0)

media = sum(lista) / (len(lista))
print(len(lista), 'valores positivos')
print(f'{media:.1f}')