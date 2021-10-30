i = 1
j = 7

count_i = 0
count_j = 0

while True:
    while count_i < 3:
        print(f'I={i} J={j}')
        j -= 1
        count_i += 1
        
    count_i = 0
    i += 2
    j = 7

    if i == 9:
        while count_j < 3:
            print(f'I={i} J={j}')
            count_j += 1
            j -= 1
        break