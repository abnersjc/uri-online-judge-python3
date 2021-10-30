n = int(input())

inn = 0
out = 0

for i in range(n):
    x = int(input())
    if x in range(10, 20):
        inn += 1
    if not x in range(10,20):
        out +=1
print(f'{inn} in')
print(f'{out} out')