import math

valor = float(input())
notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
divisao = 0
valorInicial = valor
resto = []
string = 'nota'

print('NOTAS:')
for i in notas:
    if i == 1:
        print('MOEDAS:')
        string = 'moeda'

    if i == 0.01:
        print('{:.0f} {}(s) de R$ {:.2f}'.format((valorInicial - sum(resto))*100, string, i))
    else:
        divisao = valor // i
        valor = valor % i
        resto.append(divisao * i)
        print('{:.0f} {}(s) de R$ {:.2f}'.format(divisao, string, i))