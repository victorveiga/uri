n1, n2, n3 = input().split();
codigo1, pc1, vl1 = int(n1), int(n2), float(n3);

n1, n2, n3 = input().split();
codigo2, pc2, vl2 = int(n1), int(n2), float(n3);

resultado = (pc1 * vl1) + (pc2 * vl2);
print('VALOR A PAGAR: R$ {:.2f}'.format(resultado));