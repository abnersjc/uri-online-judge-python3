a = int(input())
b = int(input())
c = int(input())

dig_a = 10 - len(str(a))
dig_b = 10 - len(str(b))
dig_c = 10 - len(str(c))

sinal_a = ''
sinal_b = ''
sinal_c = ''

if a < 0:
    a = a * -1
    sinal_a = '-'

if b < 0:
    b = b * -1
    sinal_b = '-'

if c < 0:
    c = c * -1
    sinal_c = '-'

print(f'A = {sinal_a}{a}, B = {sinal_b}{b}, C = {sinal_c}{c}')
print(f'A = {" " * dig_a}{sinal_a}{a}, B = {" " * dig_b}{sinal_b}{b}, C = {" " * dig_c}{sinal_c}{c}')
print(f'A = {sinal_a}{"0" * dig_a}{a}, B = {sinal_b}{"0" * dig_b}{b}, C = {sinal_c}{"0" * dig_c}{c}')
print(f'A = {sinal_a}{a}{" " * dig_a}, B = {sinal_b}{b}{" " * dig_b}, C = {sinal_c}{c}{" " * dig_c}')
