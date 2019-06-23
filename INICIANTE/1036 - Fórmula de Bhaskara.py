def getDelta(ADados):
    A, B, C = ADados;
    return ((B ** 2) - (4*A*C));

def Bhaskara(ADelta,AValue, operacao):
    A, B, C = AValue;
    if operacao == '+':
        return ( (-B) + (ADelta ** 0.5) ) / (2*A);
    else:
        return ( (-B) - (ADelta ** 0.5) ) / (2*A);

def calculaR(ADelta, AValue):
    # Se ADelta = 0, só tem um resultado
    print('R1 = {:.5f}'.format(Bhaskara(ADelta, AValue, '+')));

    if ADelta > 0:
        print('R2 = {:.5f}'.format(Bhaskara(ADelta, AValue, '-')));

A, B, C = [float(n) for n in input().split(' ')];
delta = getDelta([A, B, C]);

if (delta < 0) or (A == 0):
    print('Impossivel calcular');
else:
    calculaR(delta, [A, B, C]);