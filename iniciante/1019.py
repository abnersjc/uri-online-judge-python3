segundos = int(input())
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = (segundos % 3600) % 60

print('{}:{}:{}'.format(horas, minutos, segundos))