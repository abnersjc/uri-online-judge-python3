count = 0
pares = 0

while count != 5:
    n = int(input())
    count += 1
    if n % 2 == 0:
        pares += 1

print(f'{pares} valores pares')