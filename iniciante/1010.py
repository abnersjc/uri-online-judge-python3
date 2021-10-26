pc1, numpc1, valorpc1 = input().split()
pc2, numpc2, valorpc2 = input().split()

totalpagar = (int(numpc1) * float(valorpc1)) + (int(numpc2) * float(valorpc2))

print('VALOR A PAGAR: R$ {:.2f}'.format(totalpagar))