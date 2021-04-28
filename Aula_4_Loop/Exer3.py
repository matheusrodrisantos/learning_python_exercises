def mensagem():
    print('CALCULADORA')
    print('+ ADIÇÃO ')
    print('- SUBTRAÇÃO')
    print('* MULTIPLICAÇÃO')
    print('/ DIVISÃO')
    print('Pressione outra tecla para sair')

def operacao(op, x, y):
    if (op == '+'):
        return (x + y)
    if (op == '-'):
        return (x - y)
    if (op == '*'):
        return (x * y)
    if (op == '/'):
        return (x / y)

mensagem()
while True:
    op = input('Qual operação deseja fazer ?')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor:'))
        y = int(input('Digite o segundo valor:'))
        resultado = operacao(op, x, y)
        print('o resultdao é {}'.format(resultado))
        print('----------------------------------')
        mensagem()
    else:
        break
