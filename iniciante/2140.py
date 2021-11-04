while True:
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break
    resto = m - n
    notas_troco = 0

    n100 = resto // 100
    rn100 = resto % 100
    n50 = rn100 // 50
    rn50 = rn100 % 50
    n20 = rn50 // 20
    rn20 = rn50 % 20
    n10 = rn20 // 10
    rn10 = rn20 % 10
    n5 = rn10 // 5
    rn5 = rn10 % 5
    n2 = rn5 // 2
    rn2 = rn5 % 2

    if n100 != 0:
        notas_troco += n100
        
    if n50 != 0:
        notas_troco += n50

    if n20 != 0:
        notas_troco += n20

    if n10 != 0:
        notas_troco += n10

    if n5 != 0:
        notas_troco += n5

    if n2 != 0:
        notas_troco += n2

    if rn2 != 0:
        notas_troco += rn2

    if notas_troco == 2:
        print('possible')
        
    else:
        print('impossible')