import math

n1, n2, n3 = input().split(' ');
a, b, c = int(n1), int(n2), int(n3);

ab = (a + b + abs(a-b)) / 2;
ab_c = (ab + c + abs(ab-c)) / 2;

print("%d eh o maior" %ab_c);