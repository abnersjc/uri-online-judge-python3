nome = str(input())
salarioFixo = float(input())
totalVendas = float(input())
comissao = 0.15
total = (totalVendas * comissao) + salarioFixo

print('TOTAL = R$ {:.2f}'.format(total))