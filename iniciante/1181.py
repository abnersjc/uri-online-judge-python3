l = int(input())
t = str(input())
tamanho = 12
matriz = []

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)

soma = sum(matriz[l])
resultado = soma

if t == 'M':
    resultado = soma / tamanho

print(f'{resultado:.1f}')