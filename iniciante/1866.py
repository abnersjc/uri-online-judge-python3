c = int(input())

for i in range(0, c):
    n = int(input())
    v = 1

    for x in range(1, n):
        if x % 2 != 0:
            v -= 1
        else:
            v += 1

    print(v)
