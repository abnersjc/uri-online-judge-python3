import math
n = int(input())
a = 1
b = 0
c = 0
count_a = 0

for i in range(1, (n*2)+1):
    count_a += 1

    if count_a == 1:

        b = a*a
        c = math.pow(a, 3)
        print(f'{a:.0f} {b:.0f} {c:.0f}')

    if count_a == 2:

        b = (a * a) + 1
        c = (math.pow(a, 3))+1
        print(f'{a:.0f} {b:.0f} {c:.0f}')

    if count_a == 2:
        a += 1

        count_a = 0