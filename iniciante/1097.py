i = 1
j = 7

count_1 = 0

while count_1 <= 3:
    count_1 += 1
    print(f'I={i} J={j}')
    j -= 1
    if count_1 == 3:
        i += 2
        j += 5
        count_1 = 0
    if i == 11:
        break
