segundos = int(input());
horas = segundos / 3600;
minutos = segundos / 60
minutos = minutos % 60;
segundos = segundos % 60;
print('{}:{}:{}'.format(int(horas),int(minutos),int(segundos)));