n = int(input())
for i in range(0, n):
    a, b = map(str, input().split())
    combinado = ''
    for d in range(0, len(a) + len(b)): 
        if (len(a)) > d:
            combinado += a[d]
        else:
            pass
        if (len(b)) > d:
            combinado+= b[d]
        else:
            pass

    print(combinado)