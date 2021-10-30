ddd = int(input())

lista_ddd = [61, 71, 11, 21, 32, 19, 27, 31]

lista_cidade = ['Brasilia', 'Salvador', 'Sao Paulo',
                'Rio de Janeiro', 'Juiz de Fora', 'Campinas',
                'Vitoria', 'Belo Horizonte']

if ddd in lista_ddd:
    print(lista_cidade.pop((lista_ddd.index(ddd))))
else:
    print('DDD nao cadastrado')