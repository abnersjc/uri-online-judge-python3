n = int(input())
fibonacci = [0, 1]

while len(fibonacci) < n:
    soma = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(soma)

print(*fibonacci, sep=' ')