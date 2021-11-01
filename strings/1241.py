n = int(input())

for d in range(0, n):

    a, b = map(str, input().split())
    verificador = []

    for i in range(-1, (len(b)+1)*-1, -1):
        if len(b) <= len(a):
            if b[i] == a[i]:       
                verificador.append(b[i])
        else:
            pass

    if len(b) == len(verificador):
        print('encaixa')
    else:
        print('nao encaixa')