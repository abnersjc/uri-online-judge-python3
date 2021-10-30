c = int(input())
t = str(input())
tamanho = 12
matriz = []

for i in range(tamanho):
    coluna = []
    for j in range(tamanho):
        coluna.append(float(input()))
    matriz.append(coluna)

soma = 0
for k in range(tamanho):
    soma = soma + matriz[k][c]

resultado = soma

if t == 'M':
    resultado = soma / (tamanho)

print(f'{resultado:.1f}')