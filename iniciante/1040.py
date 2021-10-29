n1, n2, n3, n4 = map(float, input().split())
pn1 = 2
pn2 = 3
pn3 = 4
pn4 = 1
media = ((n1 * pn1) + (n2 * pn2)+ (n3 * pn3)+ (n4 * pn4)) / 10

if media >= 7.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')

elif media < 5.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')

elif media >= 5.0 and media <= 6.9:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    notaExame = float(input())
    print('Nota do exame: {:.1f}'.format(notaExame))
    mediaFinal = (media + notaExame) / 2
    if mediaFinal >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {}'.format(mediaFinal))
    if mediaFinal <= 4.9:
        print('Aluno reprovado.')