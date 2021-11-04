t = int(input())

for i in range(1, t + 1):
    sheldon, raj = map(str, input().split())
    #CASO 1
    if sheldon == 'tesoura' and raj == 'papel':
        print('Caso #{}: Bazinga!'.format(i))
    #CASO 1.1
    if sheldon == 'papel' and raj == 'tesoura':
        print('Caso #{}: Raj trapaceou!'.format(i))
     
    #CASO 2
    if sheldon == 'papel' and raj == 'pedra':
        print('Caso #{}: Bazinga!'.format(i))
    #CASO 2.1
    if sheldon == 'pedra' and raj == 'papel':
        print('Caso #{}: Raj trapaceou!'.format(i))
        
    #CASO 3
    if sheldon == 'pedra' and raj == 'lagarto':
        print('Caso #{}: Bazinga!'.format(i))
    #CASO 3.1
    if sheldon == 'lagarto' and raj == 'pedra':
        print('Caso #{}: Raj trapaceou!'.format(i))
        
    #CASO 4
    if sheldon == 'lagarto' and raj == 'Spock':
        print('Caso #{}: Bazinga!'.format(i))
    #CASO 4.1
    if sheldon == 'Spock' and raj == 'lagarto':
        print('Caso #{}: Raj trapaceou!'.format(i))
        
    #CASO 5
    if sheldon == 'Spock' and raj == 'tesoura':
        print('Caso #{}: Bazinga!'.format(i))
    #CASO 5.1
    if sheldon == 'tesoura' and raj == 'Spock':
        print('Caso #{}: Raj trapaceou!'.format(i))
        
    #CASO 6
    if sheldon == 'tesoura' and raj == 'lagarto':
        print('Caso #{}: Bazinga!'.format(i))
    #CASO 6.1
    if sheldon == 'lagarto' and raj == 'tesoura':
        print('Caso #{}: Raj trapaceou!'.format(i))
        
    #CASO 7
    if sheldon == 'lagarto' and raj == 'papel':
        print('Caso #{}: Bazinga!'.format(i))
    #CASO 7.1
    if sheldon == 'papel' and raj == 'lagarto':
        print('Caso #{}: Raj trapaceou!'.format(i))
        
    #CASO 8
    if sheldon == 'papel' and raj == 'Spock':
        print('Caso #{}: Bazinga!'.format(i))
    #CASO 8.1
    if sheldon == 'Spock' and raj == 'papel':
        print('Caso #{}: Raj trapaceou!'.format(i))
        
    #CASO 9
    if sheldon == 'Spock' and raj == 'pedra':
        print('Caso #{}: Bazinga!'.format(i))
    #CASO 9.1
    if sheldon == 'pedra' and raj == 'Spock':
        print('Caso #{}: Raj trapaceou!'.format(i))
        
    #CASO 10
    if sheldon == 'pedra' and raj == 'tesoura':
        print('Caso #{}: Bazinga!'.format(i))
    #CASO 10.1
    if sheldon == 'tesoura' and raj == 'pedra':
        print('Caso #{}: Raj trapaceou!'.format(i))
        
    #CASO 11
    if sheldon == raj:
        print('Caso #{}: De novo!'.format(i))