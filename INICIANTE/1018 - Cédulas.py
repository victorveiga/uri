valor = int(input());
valor_inicial = valor;
xNOTA = ['100,00', '50,00', '20,00', '10,00', '5,00', '2,00', '1,00'];
xNOTAS = [100, 50, 20, 10, 5, 2 , 1];
xVALOR = [0,0,0,0,0,0,0];
while valor > 0:
    for i in range(len(xNOTAS)):
        while (valor - xNOTAS[i]) >= 0:
            if valor > 0:
                valor = valor - xNOTAS[i];
                xVALOR[i] = xVALOR[i] + 1;
print(valor_inicial);
for i in range(len(xVALOR)):
    print('{} nota(s) de R$ {}'.format(xVALOR[i], xNOTA[i]));