nc = int(input())

for n in range(1, nc + 1):

    quantidadePessoas, salto = map(int, input().split())
    listaPessoas = []
    for vivos in range(1, quantidadePessoas + 1):
        listaPessoas.append(vivos)

    def josephus(sobrevivente, salto):
        salto -= 1 # Pula o cara morto
        matador = salto
        while len(sobrevivente) > 1:
            sobrevivente.pop(matador) # matador mata o cara
            matador = (matador + salto) % len(sobrevivente)
        print('Case {}: {}'.format(n, sobrevivente[0]))

    josephus(listaPessoas, salto)

'''


NC = eval(input())

for i in range(1, NC+1):
    n, k = map(int, input().split())
    circulo = list(range(1, n+1))

    matador = k - 1
    while len(circulo) > 1:
        circulo.pop(matador)
        matador = matador + (k - 1)
        if matador >= len(circulo):
            matador %= len(circulo)
    print ('Case {}: {}'.format(i, circulo[0]))

========================================================================================

nc = int(input())

for n in range(1, nc+1):
    

    def josephus(n, k): 
        if n == 1: 
            return 1
        else: 
            return (josephus(n - 1, k) + k-1) % n + 1

    quantidadePessoas, salto = map(int, input().split())
         
    print('Case {}: {}'.format(n, josephus(quantidadePessoas, salto)))

===========================================================================================


nc = int(input())

for n in range(1, nc + 1):

    quantidadePessoas, salto = map(int, input().split())
    listaPessoas = []
    for vivos in range(1, quantidadePessoas + 1):
        listaPessoas.append(vivos)

    def josephus(sobrevivente, salto):
        salto -= 1 # Pula o cara morto
        matador = salto
        while len(sobrevivente) > 1:
            sobrevivente.pop(matador) # matador mata o cara
            matador = (matador + salto) % len(sobrevivente)
        print('Case {}: {}'.format(n, sobrevivente[0]))

    josephus(listaPessoas, salto)




=================================================================





nc = int(input())
case = 0
for n in range(0, nc):
    case += 1
    quantidadePessoas, salto = map(int, input().split())
    listaPessoas = []
    listaMortos = []
    contador = 0
    Matador = 0

    for i in range(1, quantidadePessoas + 1):
        listaPessoas.append(i)

    while not contador == quantidadePessoas:
        contador += 1
        if not contador in listaMortos:
            Matador += 1
            
        if Matador == salto:
            listaMortos.append(contador)
            listaPessoas.remove(contador)
            Matador = 0
    
        if contador == quantidadePessoas:
            contador = 0
        
        if len(listaPessoas) == 1:
            break

    print('Case {}: {}'.format(case, listaPessoas[0]))

'''



