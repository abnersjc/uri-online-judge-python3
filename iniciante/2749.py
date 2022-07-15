total_caracter = 39
valor = 'x = 35'

print('-' * total_caracter)
print('|' + ' ' * 0 + valor + ' ' * (total_caracter - 0 - len(valor) - 2) + '|')
print('|' + ' ' * (total_caracter - 2) + '|')
print('|' + ' ' * 15 + str(valor) + ' ' * (total_caracter - 15 - len(str(valor)) - 2) + '|')
print('|' + ' ' * (total_caracter - 2) + '|')
print('|' + ' ' * 31 + str(valor) + ' ' * (total_caracter - 31 - len(str(valor)) - 2) + '|')
print('-' * total_caracter)
