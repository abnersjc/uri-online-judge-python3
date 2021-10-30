p_1 = str(input())
p_2 = str(input())
p_3 = str(input())

if p_1 == 'vertebrado':
    if p_2 == 'ave':
        if p_3 == 'carnivoro':
            print('aguia')
        if p_3 == 'onivoro':
            print('pomba')

    if p_2 == 'mamifero':
        if p_3 == 'onivoro':
            print('homem')
        if p_3 == 'herbivoro':
            print('vaca')


if p_1 == 'invertebrado':
    if p_2 == 'inseto':
        if p_3 == 'hematofago':
            print('pulga')
        if p_3 == 'herbivoro':
            print('lagarta')

    if p_2 == 'anelideo':
        if p_3 == 'hematofago':
            print('sanguessuga')
        if p_3 == 'onivoro':
            print('minhoca')