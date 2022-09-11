k = int(input())
categorias = [1, 3, 5, 10, 25, 50, 100]

for maior in categorias:
    if k > maior:
        pass
    else:
        print(f'Top {maior}')
        break
