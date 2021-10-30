while True:
    tentativa = int(input())
    senha = 2002

    if tentativa != senha:
        print('Senha Invalida')

    if tentativa == senha:
        print('Acesso Permitido')
        break