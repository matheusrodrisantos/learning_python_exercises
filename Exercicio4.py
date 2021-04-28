print("Olá, seja bem vindo!\nDeseja comprar qual fruta ?")
fruits=int(input('Digite o número correspondente da fruta\n1 - maça\n2 - laranja\n3 - banana\n '))
if(fruits==1):
    print("maça")
elif(fruits==2):
    print("laranja")
elif(fruits==3):
    print("banana")
else:
    print("produto inexistente")