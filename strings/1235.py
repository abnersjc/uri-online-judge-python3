n = int(input())

for ct in range(0, n):
    string = str(input())
    primeira_palavra = ''
    segunda_palavra = ''

    for i in range(len(string) -1, -1, -1):
        x = int((len(string) / 2))
        if i >= x:
            segunda_palavra += string[i]
        else:
            primeira_palavra += string[i]

    print('{}{}'.format(primeira_palavra, segunda_palavra))