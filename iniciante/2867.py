c = int(input())

for i in range(0, c):
    n, m = map(int, input().split())
    valor = n
    for x in range(0, m - 1):
        valor = n * valor
    print(len(str(valor)))