n = int(input())
primos = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

for c in range(0, n):
    x = int(input())
    divisores = []
    count = 0
    for i in range(0, len(primos)):

        if x % (primos[i]) == 0 and x != (primos[i]):
            divisores.append(primos[i])
            count += 1
    divisores.append(x)
    if x == 1:
        print(f'{x} nao eh primo')

    if len(divisores) == 2 and x != 1:
        print(f'{x} eh primo')

    if len(divisores) > 2:
        print(f'{x} nao eh primo')