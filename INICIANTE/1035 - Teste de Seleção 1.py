def ValidaValores(ADados):
    A, B, C, D = ADados;

    if (B > C) and (D > A):
        if ((C + D) > (A + B)):
            if (C >= 0) and (D >= 0):
                if (A % 2) == 0:
                    return True;

    return False;

A, B, C, D = [int(n) for n in input().split(' ')];
if ValidaValores([A, B, C, D]):
    print('Valores aceitos')
else:
    print('Valores nao aceitos');