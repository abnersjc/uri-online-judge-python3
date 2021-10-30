while True:
  try:
    grauValido = []

    for i in range(0, 181):
        if i % 6 == 0:
            grauValido.append(i)

    grau = int(input())

    if grau in grauValido:
        print('Y')
    else:
        print('N')

  except EOFError:
    break