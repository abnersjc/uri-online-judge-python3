n = int(input())
ho = str()

for c in range(1, n + 1):
    if c < n:
        ho += 'Ho '
    if c == n:
        ho += 'Ho!'

print(ho)