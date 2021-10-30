x, y = map(int, input().split())

count = 1

for l in range(0, int(y / x)):
    lista = []

    for j in range(0, x):

        lista.append(count)
        count += 1

    var1 = ' '.join(map(str, lista))
    print(var1)