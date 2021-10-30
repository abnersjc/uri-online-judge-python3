n = int(input())

for c in range(0, n):
    kg = float(input())
    dias = 0

    while kg > 1:
        dias += 1
        kg = kg / 2

    print(f'{dias} dias')