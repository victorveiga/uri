tabela = [4.00, 4.50, 5.00, 2.00, 1.50];
item, qtde = [int(n) for n in input().split(' ')];
print('Total: R$ {:.2f}'.format( tabela[item-1] * qtde ));