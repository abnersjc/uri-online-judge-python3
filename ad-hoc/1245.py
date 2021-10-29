while True:
  try:
    
    n = int(input())
    lista = []
    listaEsquerdo = []
    listaDireito = []
    for i in range(1, n + 1):
        bot = str(input())
        lista.append(bot)

    for d in lista:
        if d[3] == 'E':
            listaEsquerdo.append(int(d[0]+d[1]))
        else:
            listaDireito.append(int(d[0]+d[1]))

    par = 0

    for x in listaEsquerdo:
        if x in listaDireito:
            par += 1
            listaDireito.remove(x)
        else:
            pass

    print(par)
  except EOFError:
    break