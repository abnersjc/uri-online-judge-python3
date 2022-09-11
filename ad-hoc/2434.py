n, s = map(int, input().split())

movimentacoes = [s]
Menor = 0
listaMenor = []


for i in range(0, n):
    m = int(input())
    movimentacoes.append(m)

for a in movimentacoes:
    Menor += a
    listaMenor.append(Menor)

print(min(listaMenor))
