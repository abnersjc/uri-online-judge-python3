while True:
    x = int(input())
    if x == 0:
        break
    else:
        pares = []
        while True:
            if x % 2 ==0:
                pares.append(x)
            x += 1
            if len(pares) == 5:
                break
        print(sum(pares))