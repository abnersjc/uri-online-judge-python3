hi, hf = map(int, (input().split()))

if hi >= 0 and hf <= 24:
    if hi < hf:
        tempo = hf - hi
        print(f'O JOGO DUROU {tempo:.0f} HORA(S)')
    if hi > hf:
        tempo = ((1440 - (hi*60)) / 60) + hf
        print(f'O JOGO DUROU {tempo:.0f} HORA(S)')

    if hi == hf:
        tempo = ((1440-(hi*60))+(hi*60))/60
        print(f'O JOGO DUROU {tempo:.0f} HORA(S)')