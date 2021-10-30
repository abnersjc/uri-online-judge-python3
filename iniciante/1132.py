x = int(input())
y = int(input())

maior = 0
menor = 0

if x > y:
    maior = x
    menor = y

if y > x:
    maior = y
    menor = x

lista = []
for c in range(menor, maior + 1):
    if not c % 13 == 0:
        lista.append(c)

print(sum(lista))