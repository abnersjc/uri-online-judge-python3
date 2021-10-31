total = 1
divisor = 2

for dividendo in range(3, 41, 2):
    total += dividendo/divisor
    divisor = divisor * 2

print('{:.2f}'.format(total))