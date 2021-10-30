valor = float(input())
taxa = 0


if valor > 4500:
    taxa += (valor - 4500) * 0.28

if valor > 3000.00:
    if valor <= 4500:
        taxa += (valor - 3000) * 0.18
    if valor > 4500:
        taxa += 1500 * 0.18

if valor > 2000.00:
    if valor < 3000:
        taxa += (valor - 2000) * 0.08
    if valor > 3000:
        taxa += 1000 * 0.08
    print(f'R$ {taxa:.2f}')
if valor <= 2000:
    print('Isento')