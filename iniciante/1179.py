par = []
impar = []

for i in range(0, 15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        if len(par) == 5:
            for index_pares in range(0, 5):
                print('par[{}] = {}'.format(index_pares, par[index_pares]))
            par.clear()
    else:
        impar.append(n)
        if len(impar) == 5:
            for index_impares in range(0, 5):
                print('impar[{}] = {}'.format(index_impares, impar[index_impares]))
            impar.clear()

for resto_impar in range(0, len(impar)):
    print('impar[{}] = {}'.format(resto_impar, impar[resto_impar]))

for resto_par in range(0, len(par)):
    print('par[{}] = {}'.format(resto_par, par[resto_par]))