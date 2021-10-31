import math
while True:
    try:
        a, b, c = map(int,input().split())
        p = (a+b+c)/2
        # variável a, b, c são referente 
        # as retas da rigião triangular
        pi = 3.1415926535897
        area_triangulo_violetas = math.sqrt(p*(p-a)*(p-b)*(p-c))
        area_cirulo_rosas = pi*(((2*area_triangulo_violetas)/(a+b+c)) ** 2)
        area_circulo_girassois = pi*(((a*b*c)/(math.sqrt(( a + b + c )*( b + c - a )*( c + a - b )*( a + b - c ))))**2)

        girassois = (area_circulo_girassois - area_triangulo_violetas)
        violetas = (area_triangulo_violetas - area_cirulo_rosas)
        rosas = area_cirulo_rosas

        print('{:.4f} {:.4f} {:.4f}'.format(girassois, violetas, rosas))
    except EOFError:
        break