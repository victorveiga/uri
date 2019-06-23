PI = 3.14159;
n1, n2, n3 = input().split(' ');
A, B, C = float(n1), float(n2), float(n3);
print('TRIANGULO: {:.3f}'.format((A * C) / 2));
print('CIRCULO: {:.3f}'.format(PI * (C ** 2)));
print('TRAPEZIO: {:.3f}'.format(((A+B)*C) / 2));
print('QUADRADO: {:.3f}'.format(B ** 2));
print('RETANGULO: {:.3f}'.format(A * B));