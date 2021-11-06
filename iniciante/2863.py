while True:
    try:
        t = int(input())
        lista_tempo = []
        for i in range(0, t):
            tentativas = float(input())
            lista_tempo.append(tentativas)
        print(min(lista_tempo))
    except EOFError:
        break