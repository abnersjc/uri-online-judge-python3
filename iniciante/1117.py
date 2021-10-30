count = 0
notas = []

while True:

    n = float(input())
    
    if n >= 0 and n <= 10:
        count += 1
        notas.append(n)

    if n < 0 or n > 10:
        print('nota invalida')

    if len(notas) == 2:
        media = sum(notas) / 2
        print(f'media = {media:.2f}')
        break