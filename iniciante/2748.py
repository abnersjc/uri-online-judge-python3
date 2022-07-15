total_caracter = 39
quantidade_espacos = 9

nome = 'Roberto'
numero = 5786
universidade = 'UNIFEI'

print('-' * total_caracter)
print('|' + ' ' * quantidade_espacos + nome + ' ' * (total_caracter - quantidade_espacos - len(nome) - 2) + '|')
print('|' + ' ' * (total_caracter - 2) + '|')
print('|' + ' ' * quantidade_espacos + str(numero) + ' ' * (total_caracter - quantidade_espacos - len(str(numero)) - 2) + '|')
print('|' + ' ' * (total_caracter - 2) + '|')
print('|' + ' ' * quantidade_espacos + str(universidade) + ' ' * (total_caracter - quantidade_espacos - len(str(universidade)) - 2) + '|')
print('-' * total_caracter)
