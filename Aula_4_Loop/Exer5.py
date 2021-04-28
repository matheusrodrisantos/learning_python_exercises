pessoas=0
total=0
totalAge=0
while True:
    age = int(input('Qual a sua idade ?'))
    totalAge=totalAge+age
    pessoas+=1
    if(age>3 and age <=12):
        total+=15
    elif(age>12):
        total += 30
    else:
        total+=0
    op=input('deseja encerrar o programa ?')
    if(op=='sair'):
        break
media=totalAge/pessoas
print('A quantidade de pessoas: {}'.format(pessoas))
print('Total arrecadado: {}'.format(total))
print('A media de idade: {}'.format(media))
