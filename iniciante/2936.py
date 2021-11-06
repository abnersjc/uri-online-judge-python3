convidados = [300, 1500, 600, 1000, 150]
total_mandioca = 225
for i in range(0, 5):
    qnt = int(input())
    total_mandioca += qnt * convidados[i]

print(total_mandioca)