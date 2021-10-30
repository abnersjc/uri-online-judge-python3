x = int(input())
y = int(input())

maior = 0
menor = 0

if x > y:
    maior = x
    menor = y
elif y > x:
    maior = y
    menor = x

for c in range(menor + 1, maior):
    if c % 5 == 2 or c % 5 == 3:
        print(c)