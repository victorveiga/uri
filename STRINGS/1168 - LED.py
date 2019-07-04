leds = [6,2,5,5,4,5,6,3,7,6]; # 0,1,2,3,4,5,6,7,8,9
i = int(input());
for i in range(i):
    numero = input();
    total = 0;
    for n in range(len(numero)):
        total = total + leds[int(numero[n])];

    print('{} leds'.format(total));