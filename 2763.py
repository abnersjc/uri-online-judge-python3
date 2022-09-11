cpf = str(input())
string = ''
cont = 0

for dig in range(0, 14):
    if cpf[dig].isalnum():
        string += cpf[dig]

    if len(string) >= 3:
        print(string)
        string = ''
        cont += 1

    if cont == 3 and len(string) >= 2:
        print(string)
