i = 0
j = 1

dd = 0
count_i = 0
count_j = 0
count_dd = 0
var_j = 4

for c in range(0, 33):
    if dd == 0:

        print(f'I={str(i)} J={str(j)}')
    if dd > 0:

        print(f'I={str(i)}.{str(dd)} J={str(j)}.{str(dd)}')

    j += 1
    count_i += 1
    count_j += 1
    count_dd += 1

    if count_j == 15:
        j += 1
        var_j += 1
        count_j = 0


    if j == (var_j):
        j -= 3

    if count_dd == 3:
        count_dd = 0
        dd += 2
        if dd == 10:
            dd = 0

    if count_i == 15:
        i += 1
        count_i = 0