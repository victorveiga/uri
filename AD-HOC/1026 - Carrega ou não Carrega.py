'''
#Funciona, mas não é aceito, ou talvez não funcione mesmo...
def trnBase10para2(ANum):
    xBase2 = [];
    while int(ANum) > 0:

        if (ANum % 2) != 0:
            xBase2.insert(0, 1)
        else:
            xBase2.insert(0, 0)

        ANum = int(ANum / 2);

    for n in range(len(xBase2), 32):
        xBase2.insert(0, 0)
    return xBase2;

def trnBase2para10(ANum):
    soma = 0;
    ANum.reverse();
    for n in range(len(ANum)-1,-1,-1):
        if ANum[n] == 1:
            soma = soma + (2 ** n);

    return soma;


def somaBase2(ANum1, ANum2):
    xSoma = [];
    for n in range(32):
        soma = ANum1[n] + ANum2[n];
        if (soma > 1) or (soma == 0):
            xSoma.append(0);
        else:
            xSoma.append(1);

    return xSoma;

while True:
    try:
        n1, n2 = [int(n) for n in input().split(' ')];
        xN1 = trnBase10para2(n1);
        xN2 = trnBase10para2(n2);
        print(trnBase2para10(somaBase2(xN1,xN2)));
    except (EOFError):
        break;
'''
#Funciona
while True:
    try:
        n1, n2 = [int(n) for n in input().split(' ')];
        print(n1^n2);
    except (EOFError):
        break;
