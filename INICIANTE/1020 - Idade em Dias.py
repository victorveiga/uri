dias = int(input());
ano = int(dias/365);
mes = int((dias%365) / 30);
dia = int((dias%365) % 30);
print("%d ano(s)" %ano);
print("%d mes(es)" %mes);
print("%d dia(s)" %dia);