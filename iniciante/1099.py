n = int(input())

for c in range(0, n):
    x, y = map(int, input().split())
    # checar o valor maior
    maior = 0
    menor = 0

    if x > y:
        maior = x
        menor = y
    if y > x:
        maior = y
        menor = x
    # checar os impares
    impares = []
    for i in range(menor + 1, maior):
        if i % 2 != 0:
            impares.append(i)

    print(sum(impares))