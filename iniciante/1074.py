n = int(input())

for i in range(n):
    valor = int(input())

    if valor % 2 == 0 and valor != 0:
        if valor > 0 and valor != 0:
            print('EVEN POSITIVE')
        if valor < 0 and valor != 0:
            print('EVEN NEGATIVE')


    if valor % 2 != 0 and valor != 0:
        if valor > 0 and valor != 0:
            print('ODD POSITIVE')

        if valor < 0 and valor != 0:
            print('ODD NEGATIVE')

    if valor == 0:
        print('NULL')