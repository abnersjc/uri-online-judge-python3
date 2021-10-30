n = int(input())
x = input().split()

lista = []

for c in range(0, n):
    lista.append(int(x[c]))


print('Menor valor:', min(lista))
print('Posicao:', lista.index(min(lista)))