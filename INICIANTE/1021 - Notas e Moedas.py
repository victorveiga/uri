valor = float(input());
xNOTAS  = [100, 50, 20, 10, 5, 2];
xMOEDAS = [1, 0.50, 0.25, 0.10, 0.05, 0.01];
xVALOR  = [0,0,0,0,0,0];
xVALORM = [0,0,0,0,0,0];

for i in range(len(xNOTAS)):
    while (valor - xNOTAS[i]) >= 0:
        if valor > 0:
            valor = valor - xNOTAS[i];
            xVALOR[i] = xVALOR[i] + 1;

for i in range(len(xMOEDAS)):
    while (valor - xMOEDAS[i]) >= 0.00:
        if valor > 0:
            valor = round(valor - xMOEDAS[i],2);
            xVALORM[i] = xVALORM[i] + 1;

print('NOTAS:');
for i in range(len(xVALOR)):
    print('{} nota(s) de R$ {:.2f}'.format(xVALOR[i], xNOTAS[i]));
print('MOEDAS:');
for i in range(len(xVALOR)):
    print('{} moeda(s) de R$ {:.2f}'.format(xVALORM[i], xMOEDAS[i]));