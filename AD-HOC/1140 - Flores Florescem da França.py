frase = 'a';
while frase[0] != '*':
    frase = input();
    frase = frase.strip();
    isTautograma = True;
    for n in frase.split(' '):
        if n.upper()[0] != frase[0].upper():
            isTautograma = False;
            break;

    if (frase[0] != '*'):
        if isTautograma:
            print('Y');
        else:
            print('N');