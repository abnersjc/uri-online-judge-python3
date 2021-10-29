num1, num2, num3 = map(int, input().split())
lista_desordenada = [num1, num2, num3]
lista_ordenada = sorted(lista_desordenada)

for ordenado in lista_ordenada:
    print(ordenado)
print('')
for desordenado in lista_desordenada:
    print(desordenado)