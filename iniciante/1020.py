dias = int(input())
ano = dias // 365
mes = (dias % 365) // 30
dia = (dias % 365) % 30

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))