t = int(input())

for i in range(1, t + 1):
    pa, pb, g1, g2 = map(float, input().split())
    anos = 0

    while pb >= pa:
        pa = ((pa * g1) // 100) + pa
        pb = ((pb * g2) // 100) + pb
        anos += 1
    
    if anos > 100:
        print('Mais de 1 seculo.')
        continue

    print('{} anos.'.format(anos))