lista_idade = []

while True:
    idade = int(input())
    if idade > 0:
        lista_idade.append(idade)
    if idade < 0:
        break

media_idade = (sum(lista_idade)) / (len(lista_idade))

print(f'{media_idade:.2f}')