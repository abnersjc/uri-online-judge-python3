a, b, c = map(float, input().split())
lista_decrescente = [a, b, c]
lista_decrescente.sort(reverse=True)
a = lista_decrescente[0]
b = lista_decrescente[1]
c = lista_decrescente[2]

if a >= (b+c):
    print('NAO FORMA TRIANGULO')
else:
    if (a ** 2) == ((b **2) + (c ** 2)):
        print('TRIANGULO RETANGULO')
    if (a ** 2) > ((b ** 2) + (c ** 2)):
        print('TRIANGULO OBTUSANGULO')
    if (a ** 2) < ((b ** 2) + (c ** 2)):
        print('TRIANGULO ACUTANGULO')
        
    if a == b == c:
        print('TRIANGULO EQUILATERO')

    if a == b and b != c:
        print('TRIANGULO ISOSCELES')
    if b == c and c != a:
        print('TRIANGULO ISOSCELES')
    if c == a and a != b:
        print('TRIANGULO ISOSCELES')