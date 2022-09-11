p = int(input())

valores = {'1001': 1.50,
           '1002': 2.50,
           '1003': 3.50,
           '1004': 4.50,
           '1005': 5.50
           }

valorCompra = 0


for i in range(0, p):
    q = int, input().split()
    valorCompra += int(q[1][1]) * valores[f'{(q[1][0])}']

print('{:.2f}'.format(valorCompra))
