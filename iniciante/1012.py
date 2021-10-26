a, b, c = list(map(float,input().split()))

trianguloRetangulo = (a * c) / 2
circulo = 3.14159 * (c * c)
trapezio = ((a + b)) * c / 2
quadrado = b * b
retangulo = a * b

print('TRIANGULO: {:.3f}'.format(trianguloRetangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))