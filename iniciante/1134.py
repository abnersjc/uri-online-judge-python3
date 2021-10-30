alcool = 0
gasolina = 0
diesel = 0

while True:
    valor = int(input())

    if valor == 1:
        alcool += 1
    if valor == 2:
        gasolina += 1
    if valor == 3:
        diesel += 1

    if not valor != 1 and valor != 2 and valor != 3 and valor != 4:
        continue
    if valor == 4:
        print('MUITO OBRIGADO')
        print(f'Alcool: {alcool}')
        print(f'Gasolina: {gasolina}')
        print(f'Diesel: {diesel}')
        break