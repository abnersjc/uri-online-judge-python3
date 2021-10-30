notas_validas = []
count = 0
novo_calculo = int(0)
media = 0

while True:
    n = float(input())

    if n < 0 or n > 10:
        print('nota invalida')

    if n >= 0 and n <= 10:
        notas_validas.append(n)
        count += 1

    if count == 2:
        media += sum(notas_validas) / 2
        print(f'media = {media:.2f}')

        while True:
            print('novo calculo (1-sim 2-nao)')
            novo_calculo = int(input())

            if novo_calculo == 1:
                notas_validas.clear()
                count = 0
                media = 0
                break
            if novo_calculo == 2:
                break

    if novo_calculo == 2:
        break