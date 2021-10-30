x = int(input())
y = int(input())

lista = []

while not y == (x - 1):
    if y == x:
        break
    y += 1
    if y % 2 != 0:
        lista.append(y)

print(sum(lista))