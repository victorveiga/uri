for i in range(int(input())):
    A, B = input().split(' ');
    if A[-len(B)::] == B:
        print('encaixa');
    else:
        print('nao encaixa');