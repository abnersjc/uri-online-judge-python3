n = int(input())

total = 0
s = 0    # sapos
r = 0    # ratos
c = 0    # coelhos

for i in range(1, n + 1):
    q = str(input())

    quantidade_tipo = int(q.split().pop(0))
    tipo = str(q.split().pop(1)).upper()
    total += quantidade_tipo

    if tipo == 'C':
        c += quantidade_tipo
    elif tipo == 'R':
        r += quantidade_tipo
    elif tipo == 'S':
        s += quantidade_tipo

pc = (c * 100) / total
pr = (r * 100) / total
ps = (s * 100) / total

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {pc:.2f} %')
print(f'Percentual de ratos: {pr:.2f} %')
print(f'Percentual de sapos: {ps:.2f} %')
