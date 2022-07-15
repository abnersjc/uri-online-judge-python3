n = int(input())

if n < 10000:

    for c in range(1, 10000):
        if c % n == 2:
            print(c)
