n = int(input())
um = 'one'
dois = 'two'
tres = 'three'

verifica_um = 0
verifica_dois = 0
verifica_tres = 0

for ct in range(0, n):
    string = str(input())
    
    #VERIRICADOR DE UM E DOIS
    if len(string) == 3:
        for a in range(0, 3):
            if string[a] == um[a]:
                verifica_um += 1 
            if string[a] == dois[a]:
                verifica_dois += 1
        if verifica_um == 2 or string == um:
            print(1)
            verifica_um = 0
            verifica_dois = 0

        if verifica_dois == 2 or string == dois:
            print(2)
            verifica_dois = 0
            verifica_um = 0
            
    #VERIRICADOR DE TRES
    if len(string) == 5:
        for c in range(0, 5):
            if string[c] == tres[c]:
                verifica_tres += 1
            else:
                continue
        if verifica_tres == 4 or string == tres:
            print(3)
            verifica_tres = 0