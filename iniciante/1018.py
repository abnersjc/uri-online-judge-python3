valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
divisao = 0
restos = 0
print(valor)
for i in notas:
    divisao = valor // i
    valor = valor % i
    print('{} nota(s) de R$ {},00'.format(divisao, i))