import math
n = int(input())

for c in range(0, n + 1):
    if c % 2 == 0:
        pot = 2
        if c != 0:
            print(f'{c:.0f}^{pot:.0f} = {math.pow(c, pot):.0f}')