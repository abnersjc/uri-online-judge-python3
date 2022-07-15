lista = []

for c in range(1, 101):
    n = int(input())
    lista.append(n)

maior = max(lista)
posicao = (lista.index(maior)) + 1

print(maior)
print(posicao)
