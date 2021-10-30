hi, mi, hf, mf = map(int, (input().split()))

h = 0
m = 0

if hi < hf:
    h = hf - hi
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h -= 1
        m = (60-mi) + mf

if hi > hf:
    h = (24-hi) + hf
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h -= 1
        m = (60-mi) + mf

if hi == hf:
    h = hi - hf
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = ((24-hi) + hf) - 1
        m = (60-mi) + mf

if hi == hf and mi == mf:
    h = (24-hi) + hf
    m = mi - mf

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')