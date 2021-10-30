n = int(input())

for i in range(0, n):
    a, b = map(int, input().split())
    nova_a = str(a)
    nova_b = str(b)

    quantidade_de_b = len(nova_b)
    caracter_de_a = nova_a[-quantidade_de_b::]
    

    if caracter_de_a == nova_b:
        print('encaixa')
    else:
        print('nao encaixa')
