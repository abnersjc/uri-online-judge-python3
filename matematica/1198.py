while True:
    try:
        a, b = map(int, input().split())

        maior = 0
        menor = 0

        if a > b:
            maior = a
            menor = b

        if b > a:
            maior = b
            menor = a

        dif = maior - menor
        print(dif)

    except EOFError:
        break