n=int(input('Digite um valor: '))
while True:
    if(n>=100):
        qtdC=n//100
        n=n%100
        print('cedulas de 100 {}'.format(qtdC))
        if not n:
            break
    if(n>=50):
        qtdCin = n // 50
        n = n % 50
        print('cedulas de 50 {}'.format(qtdCin))
        if not n:
            break
    if(n>=20):
        qtdVin = n // 20
        n = n % 20
        print('cedulas de 20 {}'.format(qtdVin))
        if not n:
            break
    if(n>=10):
        qtdDez = n // 10
        n = n % 10
        print('cedulas de Dez {}'.format(qtdDez))
        if not n:
            break
    if(n>=5):
        qtdCinc = n // 5
        n = n % 5
        print('cedulas de 5 {}'.format(qtdCinc))
        if not n:
            break
    if n:
        qtdUm = n
        print('cedulas de 1 {}'.format(qtdUm))
        break


