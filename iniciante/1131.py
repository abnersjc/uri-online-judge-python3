grenais = 0
inter = 0
gremio = 0
empates = 0
vencedor = ''


while True:
    i, g = map(int, input().split())
    print('Novo grenal (1-sim 2-nao)')
    n = int(input())
    grenais += 1

    if i > g:
        inter += 1
    if g > i:
        gremio += 1
    if i == g:
        empates += 1

    if n == 1:
        continue
    if n == 2:
        break

if inter > gremio:
    vencedor += 'Inter venceu mais'

if gremio > inter:
    vencedor += 'Gremio venceu mais'

if inter == gremio:
    vencedor += 'Nao houve vencedor'

print(f'{grenais} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empates}')
print(f'{vencedor}')