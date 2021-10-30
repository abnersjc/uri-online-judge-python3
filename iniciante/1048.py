s = float(input())

if s <= 400:
    p = 15
    a = s * (p / 100)
    ns = s + a
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(a))
    print('Em percentual: {} %'.format(p))
elif s <= 800:
    p = 12
    a = s * (p / 100)
    ns = s + a
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(a))
    print('Em percentual: {} %'.format(p))

elif s <= 1200:
    p = 10
    a = s * (p / 100)
    ns = s + a
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(a))
    print('Em percentual: {} %'.format(p))

elif s <= 2000:
    p = 7
    a = s * (p / 100)
    ns = s + a
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(a))
    print('Em percentual: {} %'.format(p))

elif s > 2000:
    p = 4
    a = s * (p / 100)
    ns = s + a
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(a))
    print('Em percentual: {} %'.format(p))