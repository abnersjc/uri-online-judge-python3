count = 0
positivos = 0

while not count == 6:
    n = float(input())
    count += 1
    if n > 0:
        positivos += 1

print(f'{positivos} valores positivos')