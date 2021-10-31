n = int(input())

for i in range(0, n):
    x, y = map(int, input().split())
    impar = []
    while True:
        if x % 2 != 0:
            impar.append(x)
        x += 1

        if len(impar) == y:
            break
    print(sum(impar))