t = int(input())
fibonacci = [0, 1]

while not len(fibonacci) == 61:
    soma = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(soma)
for i in range(0, t):
    n = int(input())

    print('Fib({}) = {}'.format(n, fibonacci[n]))