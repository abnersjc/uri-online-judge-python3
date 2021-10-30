n = int(input())

for i in range(0, n):
    x, y = map(float, input().split())

    if y != 0:
        divisao = x / y
        print(divisao)

    elif y == 0:
        print('divisao impossivel')