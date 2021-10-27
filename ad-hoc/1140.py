while True:
    frase = input().split()
    if frase[0] == '*':
        break
    else:
        lista = []
        letrasIguais = 0
        for palavras in frase:
            lista += palavras[0].upper()
        
        for letra in range(0, len(lista)):
            if (lista[0] == lista[letra]):
                letrasIguais += 1
        if letrasIguais == len(lista):
            print('Y')
        else:
            print('N')