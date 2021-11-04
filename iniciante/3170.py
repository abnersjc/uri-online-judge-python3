b = int(input())
g = int(input())

if g % 2 != 0:
    g -= 1

if g / 2 == b:
    print('Amelia tem todas bolinhas!')

if g / 2 != b:
    faltam = (g / 2)- b
    if faltam <= 0:
        print('Amelia tem todas bolinhas!')
    else:
        print('Faltam {:.0f} bolinha(s)'.format(faltam))