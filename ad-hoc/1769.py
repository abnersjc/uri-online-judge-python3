while True:
    try:
        cpf = str(input())
        num_cpf = []

        b_1 = []
        count_1 = 1

        b_2 = []
        count_2 = 9

        for i in range(0, len(cpf)):
            digito_cpf = cpf[i]
            if digito_cpf.isnumeric():
                num_cpf.append(int(digito_cpf))

        for c in range(0, 9):
            b_1.append((num_cpf[c]) * count_1)
            count_1 += 1

        for d in range(0, 9):
            b_2.append((num_cpf[d]) * count_2)
            count_2 -= 1

        digito_10 = num_cpf[9]
        digito_11 = num_cpf[10]

        verifica_b_1 = (sum(b_1) % 11)
        verifica_b_2 = (sum(b_2) % 11)

        if verifica_b_1 == 10:
            verifica_b_1 = 0

        if verifica_b_2 == 10:
            verifica_b_2 = 0

        if verifica_b_1 == num_cpf[9] and verifica_b_2 == num_cpf[10]:
            print('CPF valido')
        else:
            print('CPF invalido')

    except EOFError:
        break